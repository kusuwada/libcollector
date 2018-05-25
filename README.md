Libcollector
====
Collect name & versions of the used libraries from github repositories．

## Description
**`libcollector`** is a python3 commandline tool to collect information of the library which used in specified github repositories.  
You can specify repositories which you have Read permission. You can also specify target library manager file types (e.g. `requirement.txt`), and output media.
Each support type is [bellow](#settings).

## Demo
TBD


## Installation
### Requirements
* git   (or download this repository via http)
* python3

### Installation
Get this repository and install required modules.
```
$ git clone https://github.com/kusuwada/libcollector.git
$ cd libcollector
$ pip install -r requirements.txt
```

## Usage
### Prepare
Before use, you have to create your "github access token for commandline", if the target repository is private.  
See [GitHub Help: Authenticating to GitHub](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).  
https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/  
As it says, please select `repo` in scope selection.

### Basic usage

```
$ cd libcollector
$ python libcollector.py [--token {github_access_token}]
```
* `--token` is an optional. If the target includes private repository, you have to create "github access token" and set this option.

### Settings
See and Edit `libcollector/settings.yml`

#### target_repositories
List of the target repositories. Format is bellow
```
{owner}/{repository}
```
e.g.
```
target_repositories:
  - kusuwada/node-slack-log-exporter
  - kusuwada/ruby-slack-log-exporter
  - requests/requests
```
You can specify both public & private repository. If you specify private repository, see [Prepare](#prepare).

#### target_manager
List of the target library managers. Now, we support bellow managers.
* requirements.txt (python)
* Gemfile (ruby)
* package.json (javascript)

If you want to collect libraries from other manager file, you can add your implementation.

#### output
List of the export media/formats. Format is bellow.
```
{output_type}: {output_path}
```
Now, we support bellow formats.
* csv
* text

If you want to export other medias or db, you can add your implementation.

## License
Please see the LICENSE file for details.
[URL]
or
[MIT](https://github.com/kusuwada/libcollector/blob/master/LICENCE)

## Author
[kusuwada](https://github.com/kusuwada)

## Future Plan
* Support library collection from install command. e.g. `apt-get`, `yum`
* Add test
