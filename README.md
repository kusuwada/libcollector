Libcollector
====
Collect name, versions, and other information (e.g. license, author) of the used OSS libraries from github repositories．

## Description
**`libcollector`** is a python3 commandline tool to collect information of the library which used in specified github repositories.  
This tool collects libraries from package management files like `requirements.txt` with python or `package.json` in nodejs. The available managers are [below](#target_manager).  
[Optional information](#optional_information) like license or author will collected from each package manager's web api or web site. If it can't find these  information, the optional information will be empty.  
[You can specify repositories](#target_repositories) which you have Read permission.

## Demo

Here is an execution sample. Target repository is `vuejs/vue`, and output format is csv.

```
$ python libcollector.py
```

![demo_vue](https://github.com/kusuwada/libcollector/raw/resources/demo_vue.png)


## Installation
### Requirements
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
List of the target repositories. Format is below
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
List of the target library managers. Now, we support below managers.
* requirements.txt (python)
* Gemfile (ruby)
* package.json (javascript)

If you want to collect libraries from other manager file, you can add your implementation.

#### output
List of the export media/formats. Format is below.
```
{output_type}: {output_path}
```
Now, we support below formats.
* csv
* text

If you want to export other medias or db, you can add your implementation.

#### optional_information
You can specify output optional information below or not.

* info_license: library's license
* info_author: library's author
* info_homepage_url: library's homepage url
* info_code_url: library's source code url

If the tool can't get these information, output record becomes empty.

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
