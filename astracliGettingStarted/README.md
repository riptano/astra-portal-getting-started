# Overview
The DataStax Astra Command Line Interface (CLI) is a tool for both Astra DB and Astra Streaming. With a focus on automation, the Astra CLI gives you a set of commands to quickly create and manage your Astra resources. The CLI enables you to work with your Astra DB resources, query data through CQLSH, load data with DSBulk, configure and manage your Astra Streaming artifacts, and define Users and Roles.

**In this guide, we'll**
- Install the Astra CLI
- Configure the CLI with your Astra account
- Use the CLI to connect to and manage Astra DB

# Prerequisites
To use the Astra CLI, you need to create a token with the _"Organization Administrator"_ role.

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

**Where is Astra CLI installed on my machine?**

    - The Astra CLI is installed in `~/.astra/cli`. This folder is deleted and recreated during installation.
    - Your configuration is saved in the `~/.astrarc` file and will not be lost during reinstallation.

### Install on Windows
- Download the Windows archive [astra-cli-${version}-windows.zip](https://github.com/datastax/astra-cli/releases/download/0.2/astra-cli-0.2-windows.zip)

- Unzip the archive in a folder or your choice, for example `C:\Programs\astra-cli`

- Add `C:\Programs\astra-cli\astra.exe` to your path using [this tutorial](https://www.howtogeek.com/118594/how-to-edit-your-system-path-for-easy-command-line-access/)

## 2 Setup
In this step, we will configure the CLI to use your Astra token and get familiar with some basic commands.

### 2a Configuring your token
Before issuing commands, you will need to initialize the configuration file `~/.astrarc`. 

To run the following command during setup, you will be asked to provide your token (AstraCS:...).

```shell
astra setup
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/setup.png?raw=true" width="100%" />


<!--
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
-->
You're all set! The configuration (mainly your token) is stored in file `~/.astrarc`.

### 2b Your first commands
- Display current version of the cli, validating setup is complete.

```bash
astra --version
```

- Display your configuration list. This is a list of the organizations for your Astra account. If you are using multiple organizations, the CLI makes it easy to switch between them.

```bash
astra config list
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/config.png?raw=true" width="100%" />

<!--
```shell
+-----------------------------------------+
| configuration                           |
+-----------------------------------------+
| default (cedrick.lunven@datastax.com)   |
| cedrick.lunven@datastax.com             |
+-----------------------------------------+
```
-->

### 2c Accessing Help Documentation
The CLI provides extensive documentation for every command. It also provides bash-style autocompletion, use the `TAB` key twice to get a list of commands and options.

```bash
astra <TAB> <TAB>
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/helptab.png?raw=true" width="100%" />

<!--
```shell
--no-color  config      db          help        role        setup       shell       user  
```
-->

The help documentation is organized by groups of commands. You can access help documentation at the top level, at the level of a specific command, or for the options within a command. 

- Display the top level main help

```bash
astra help
```


**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/help.png?raw=true" width="100%" />

<!--
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
-->

- Display help for the command group `astra db`

```bash
astra help db
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/dbhelp.png?raw=true" width="100%" />

<!--
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
-->
    
## 3 Working with Astra DB
Now that we're configured with our Astra account and know how to access the list of commands, let's start using Astra DB.

### 3a List Databases
To get the list of non terminated database in your oganization, use the command `list` in the group `db`. You can change the output of the database list to _csv_ by adding `-o csv` or to _json_ by adding `-o json`.

```bash
astra db list
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/dblist.png?raw=true" width="100%" />

<!--
```shell
+---------------------+--------------------------------------+---------------------+----------------+
| Name                | id                                   | Default Region      | Status         |
+---------------------+--------------------------------------+---------------------+----------------+
| mtg                 | dde308f5-a8b0-474d-afd6-81e5689e3e25 | eu-central-1        | ACTIVE         |
| workshops           | 3ed83de7-d97f-4fb6-bf9f-82e9f7eafa23 | eu-west-1           | ACTIVE         |
| sdk_tests           | 06a9675a-ca62-4cd0-9b94-aefaf395922b | us-east-1           | ACTIVE         |
| test                | 7677a789-bd57-455d-ab2c-a3bdfa35ba68 | eu-central-1        | ACTIVE         |
+---------------------+--------------------------------------+---------------------+----------------+
```
-->

### 3b Create Database
Let's create a database using `db create`. If not specified, the region will be the default free region, and the keyspace will be the database name. You can change those settings with `-r` and `-k` respectivitely.

```bash
astra db create demo
```

By default, the `create` command is a synchronous call which will wait until the database is created and active. If you would like to issue the command asynchronously, just add `--asynch`

### 3c Resume Database
In the free tier, your database will be hibernated after 23 hours of inactivity. To wake up the db, use the `resume` command.

For example, if you had a database named `hemidactylus`:


```bash
astra db resume hemidactylus
```

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/hibernate.png?raw=true" width="100%" />

<!--
```shell
+---------------------+--------------------------------------+---------------------+----------------+
| Name                | id                                   | Default Region      | Status         |
+---------------------+--------------------------------------+---------------------+----------------+
| hemidactylus        | 643c6bb8-2336-4649-97d5-39c33491f5c1 | eu-central-1        | RESUMING       |
+---------------------+--------------------------------------+---------------------+----------------+

And after a few minutes, the database will be **ACTIVE** again. 
+---------------------+--------------------------------------+---------------------+----------------+
| Name                | id                                   | Default Region      | Status         |
+---------------------+--------------------------------------+---------------------+----------------+
| hemidactylus        | 643c6bb8-2336-4649-97d5-39c33491f5c1 | eu-central-1        | ACTIVE         |
+---------------------+--------------------------------------+---------------------+----------------+
```
-->


### 3d Get Database Details
To get general information for the database, use the `get` command. To access the values of individual attributes, use `get --key <attribute>`. This produces raw output which can be particularly useful when using the CLI in scripts.

```bash
astra db get demo
```

In the output, you specifically see the list of keyspaces available and the different regions.

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/dbdetails.png?raw=true" width="100%" />

<!--
```shell
+------------------------+-----------------------------------------+
| Attribute              | Value                                   |
+------------------------+-----------------------------------------+
| Name                   | demo                                    |
| id                     | 071d7059-d55b-4cdb-90c6-41c26da1a029    |
| Status                 | ACTIVE                                  |
| Default Cloud Provider | AWS                                     |
| Default Region         | us-east-1                               |
| Default Keyspace       | demo                                    |
| Creation Time          | 2022-07-26T15:41:18Z                    |
|                        |                                         |
| Keyspaces              | [0] demo                                |
|                        |                                         |
| Regions                | [0] us-east-1                           |
+------------------------+-----------------------------------------+
```
-->

### 3e Download Secure Connect Bundle
The CLI can download the Secure Connect Bundle which includes the security certificates needed to connect your application to your database. Use the `db download-scb` command to download the secure connect bundles (one per region) with the pattern `scb_${dbid}-${dbregion}.zip` in the current folder. Add `-d` to specify a different download directory and/or add `-f` to use a different file name.

```bash
mkdir db-demo
cd db-demo
astra db download-scb demo
ls
```

### 3f Querying with CQLSH
CQLSH is a standalone interface to work with Astra using CQL (Cassandra Query Language). With CQLSH, you can execute any number of CQL operations on the database including creating tables, querying data, and much, much more. The Astra CLI will download, install, setup and wrap CQLSH for you so that you can more easily interact with Astra.

#### Launch CQLSH
If no options are provided,  you enter `cqlsh` interactive mode

```bash
astra db cqlsh demo
```

You can use `exit` to exit out of interactive mode.

**Sample Output**

<img alt="Astra Setup" src="https://github.com/riptano/astra-portal-getting-started/blob/main/astracliGettingStarted/cqlsh.png?raw=true" width="100%" />

<!--
```shell
Cqlsh is starting please wait for connection establishment...
Connected to cndb at 127.0.0.1:9042.
[cqlsh 6.8.0 | Cassandra 4.0.0.6816 | CQL spec 3.4.5 | Native protocol v4]
Use HELP for help.
token@cqlsh>
```

Now exit the cqlsh shell to exit interactive mode
```bash
exit
```
-->

#### Execute CQL
To execute a CQL Statement with `cqlsh`, use the flag `-e`.

```bash
astra db cqlsh demo -e "describe keyspaces";
```

#### Execute CQL Files
To execute CQL Files with `cqlsh`, use the flag `-f`. You can also use the CQL syntax SOURCE.

```bash
astra db cqlsh demo -f sample.cql
```
_Note, "sample.cql" in the above command is just an example. The command above will state that it cannot find the file if you execute it._

### 3g Delete Database
To delete a db, use the `delete` command.

```bash
astra db delete demo
```
Similar to database creation, `delete` command is a synchronous call which will wait until the database is deleted. If you would like to issue the command asynchronously, just add `--asynch`.

## 4 Summary
In summary, we learned how to install the Astra CLI, access the integrated documentation, work with databases, and run a simple query with CQLSH. This just scratches the surface of what you can do with the CLI, both in your local development environment and in your automation and CI/CD scripts. 

If you liked this guide and want to learn more about loading data, click the **Recommended Guides** section below to start using DSBulk.

Also, check out the **Recommended Links** for additonal examples on working with Astra Streaming and the pulsar-shell, user and role management, and more querying and data loading scenarios.

Happy scripting! 🚀
