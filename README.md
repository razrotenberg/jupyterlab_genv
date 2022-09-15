# jupyterlab_genv

[![Github Actions Status](https://github.com/run-ai/jupyterlab_genv/workflows/Build/badge.svg)](https://github.com/run-ai/jupyterlab_genv/actions/workflows/build.yml)
A JupyterLab extension.

This extension is composed of a Python package named `jupyterlab_genv`
for the server extension and a NPM package named `jupyterlab_genv`
for the frontend extension.

## Requirements

- JupyterLab >= 3.0

## Install

To install the extension, execute:

```bash
pip install jupyterlab_genv
```

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyterlab_genv
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

If the server extension is installed and enabled, but you are not seeing
the frontend extension, check the frontend extension is installed:

```bash
jupyter labextension list
```

## Contributing

### Development setup
#### Create a virtual environment
```bash
conda create -n jupyterlab_genv --override-channels --strict-channel-priority -c conda-forge -c nodefaults jupyterlab=3 cookiecutter nodejs jupyter-packaging git
```

#### Activate the virtual environment
```bash
conda activate jupyterlab_genv
```

#### Install kernel provisioner
First, you can test that the Python package is installed correctly and exposes the provisioner class by running:
```
python -c "from jupyterlab_genv import genv_provisioner; provisioner = genv_provisioner.GenvProvisioner(); print(provisioner)"
```

Second, you can test that the kernel provisioner is registered in Jupyter by running:
```
jupyter kernelspec provisioners
```

To add a kernel provisioner to a kernel, edit its `kernel.json` file:
```
vim $(conda info --base)/envs/jupyterlab_genv/share/jupyter/kernels/python3/kernel.json
```

And add:
```
"metadata": {
  "kernel_provisioner": {
    "provisioner_name": "genv-provisioner"
  }
}
```

#### List all running kernels
```
ls -la $(jupyter --runtime-dir)/kernel-*.json
```

### Development install

Note: You will need NodeJS to build the extension package.

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Change directory to the jupyterlab_genv directory
# Install package in development mode
pip install -e .
# Link your development version of the extension with JupyterLab
jupyter labextension develop . --overwrite
# Server extension must be manually installed in develop mode
jupyter server extension enable jupyterlab_genv
# Rebuild extension Typescript source after making changes
jlpm build
```

You can watch the source directory and run JupyterLab at the same time in different terminals to watch for changes in the extension's source and automatically rebuild the extension.

```bash
# Watch the source directory in one terminal, automatically rebuilding when needed
jlpm watch
# Run JupyterLab in another terminal
jupyter lab
```

> You can pass `--no-browser` to the `jupyter lab` command

With the watch command running, every saved change will immediately be built locally and available in your running JupyterLab. Refresh JupyterLab to load the change in your browser (you may need to wait several seconds for the extension to be rebuilt).

By default, the `jlpm build` command generates the source maps for this extension to make it easier to debug using the browser dev tools. To also generate source maps for the JupyterLab core extensions, you can run the following command:

```bash
jupyter lab build --minimize=False
```

### Development uninstall

```bash
# Server extension must be manually disabled in develop mode
jupyter server extension disable jupyterlab_genv
pip uninstall jupyterlab_genv
```

In development mode, you will also need to remove the symlink created by `jupyter labextension develop`
command. To find its location, you can run `jupyter labextension list` to figure out where the `labextensions`
folder is located. Then you can remove the symlink named `jupyterlab_genv` within that folder.

### Packaging the extension

See [RELEASE](RELEASE.md)
