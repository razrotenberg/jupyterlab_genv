from typing import Dict, List

from . import control

async def exec(command: str) -> str:
    return await control.exec(f'exec devices {command}')

async def query(eid: str) -> List[int]:
    return [int(index) for index in (await exec(f'query --eid {eid}')).split(',') if len(index) > 0]

async def ps() -> Dict:
    stdout = await exec("ps --format csv --no-header --timestamp")
    lines = [line for line in stdout.splitlines() if len(line)]

    infos = []

    for line in lines:
        id, eid, env, attached = line.split(',')
        id = int(id)

        infos.append({
            "eid": eid,
            "env": env,
        })

    return infos
