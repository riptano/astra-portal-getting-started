# Overview
In this guide we will learn how to use the DataStax Astra command line interface (Astra CLI) with both Astra DB and Astra Streaming. The Astra CLI is a set of commands used to create and manage your Astra resources. The Astra CLI is designed to get you working quickly with Astra, with an emphasis on automation. The CLI enables you to work with your Astra DB resources, query data through CQLSH, load data with DSBulk, configure and manage your Astra Streaming artifacts, and define Users and Roles.

**In this guide, we will**
- Install the Astra CLI
- Configure the CLI with your Astra account
- Use the CLI to connect to and manage Astra DB

# Prerequisites
To use the Astra CLI you need to create a token with the _"Organization Administrator"_ role.

<<createToken>>

## 1 Installation
The Astra CLI is available on **Windows**, **MacOS** and **Linux** environments.

### Install on MacOS with Homebrew
Homebrew is the easiest way to manage your CLI installation. It provides a convenient way to install, update, and uninstall. If you don't have homebrew available on your system, install homebrew before continuing.

You can install the Astra CLI on macOS by updating your brew repository information, and then running the install command:

```shell
brew install datastax/astra-cli/astra-cli
```

The Homebrew formula of Astra CLI installs a completion file named astra in the Homebrew-managed completions directory (the default location is /usr/local/etc/bash_completion.d/). To enable completion, please follow Homebrew's instructions [here](https://docs.brew.sh/Shell-Completion).

### Install on Linux
To install (or reinstall) the CLI use the following command in a terminal:

```shell
curl -Ls "https://dtsx.io/get-astra-cli" | bash
```

??? question "Where is Astra CLI installed on my machine ?"

    - The Astra CLI is installed in `~/.astra/cli`. This folder is deleted and recreated during installation.
    
    - Your configuration is saved in the `~/.astrarc` file and will not be lost during reinstallation.

### Install on Windows
- Download the Windows archive [astra-cli-${version}-windows.zip](https://github.com/datastax/astra-cli/releases/download/0.2/astra-cli-0.2-windows.zip)

- Unzip the archive in a folder or your choice, for example `C:/Programs/astra-cli`

- Add `C:/Programs/astra-cli/astra.exe` to your path using [this tutorial](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)

## 2 Setup

In this step, we will configure the CLI to use your Astra token and get familiar with some basic commands.

### 2a Configuring your token
Before issuing commands you will need to initialize the configuration file `~/.astrarc`. 

To to so run the following command. During setup, you will be asked to provide your token (AstraCS:...).

```shell
astra setup
```

???+ abstract "🖥️ `astra setup` command output"

    ```shell
        _____            __                
       /  _  \   _______/  |_____________   
      /  /_\  \ /  ___/\   __\_  __ \__  \ 
    /    |    \\___ \  |  |  |  | \// __ \_
    \____|__  /____  > |__|  |__|  (____  /
             \/     \/                   \/

            ------------------------
            ---       SETUP      ---
            ------------------------

    🔑 Enter token (starting with AstraCS...):
    ```

You are all set. The configuration (mainly your token) is stored in file `~/.astrarc`.

### 2b Your first commands
- Display current version of the cli, validating setup is complete.

```bash
astra --version
```

- Display your configuration list. This is a list of the organizations for your Astra account. If you are using multiple organizations, the CLI makes it easy to switch between them.

```bash
astra config list
```

???+ abstract "🖥️ Sample output" 

    ```shell
    +-----------------------------------------+
    | configuration                           |
    +-----------------------------------------+
    | default (cedrick.lunven@datastax.com)   |
    | cedrick.lunven@datastax.com             |
    +-----------------------------------------+
    ```
### 2c Accessing Help Documentation

The CLI provides extensive documentation for every command. It also provides bash-style autocompletion, use the `TAB` key twice to get a list of commands and options.

```bash
astra <TAB> <TAB>
```

???+ abstract "🖥️ Sample output" 

    ```shell
    --no-color  config      db          help        role        setup       shell       user  
    ```

The help documentation is organized by groups of commands. You can access help documentation at the top level, at the level of a specific command, or for the options within a command. 

- Display the top level main help

```bash
astra help
```

???+ abstract "🖥️ Sample output" 

    ```shell
    usage: astra <command> [ <args> ]

    Commands are:
        help     View help for any command
        setup    Initialize configuration file
        shell    Interactive mode (default if no command provided)
        config   Manage configuration file
        db       Manage databases
        role     Manage roles (RBAC)
        user     Manage users

    See 'astra help <command>' for more information on a specific command.
    ```

- Display help for the command group `astra db`

```bash
astra help db
```

???+ abstract "🖥️ Sample output" 

    ```shell
    NAME
            astra db - Manage databases

    SYNOPSIS
            astra db { cqlsh | create | create-keyspace | delete | dsbulk | get |
                    list } [--] [ --token <AUTH_TOKEN> ]
                    [ --config-file <CONFIG_FILE> ] [ --no-color ]
                    [ {-v | --verbose} ] [ {-conf | --config} <CONFIG_SECTION> ]
                    [ --log <LOG_FILE> ] [ {-o | --output} <FORMAT> ] [cmd-options]
                    <cmd-args>

            Where command-specific options [cmd-options] are:
                cqlsh: [ --debug ] [ {-f | --file} <FILE> ] [ {-k | --keyspace} <KEYSPACE> ]
                        [ --version ] [ {-e | --execute} <STATEMENT> ] [ --encoding <ENCODING> ]
                create: [ {-k | --keyspace} <KEYSPACE> ] [ --if-not-exist ] [ {-r | --region} <DB_REGION> ]
                create-keyspace: {-k | --keyspace} <KEYSPACE> [ --if-not-exist ]
                delete:
                dsbulk:
                get:
                list:

            Where command-specific arguments <cmd-args> are:
                cqlsh: <DB>
                create: <DB_NAME>
                create-keyspace: <DB>
                delete: <DB>
                dsbulk: [ <dsbulkArguments>... ]
                get: <DB>
                list:

            See 'astra help db <command>' for more information on a specific command.
    ```
    
## 3 Working with Astra DB
Now that we are configured with our Astra account and know how to access the list of commands, let's start using Astra DB.
