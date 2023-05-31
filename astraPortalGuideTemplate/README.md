<!-- 
This is the overview section. 
The overview should provide users a high level explanation of what your guide is all about at a glance. 
What will they learn, what will they get out of it?
 -->
# Overview
Hiya. Welcome to the Astra getting started guide template. Use this template to help "guide" you through authoring "getting started" guides within DataStax Astra. 😏

"Getting Started" guides are a unique way to help Astra users learn about a topic or how to perform a set of actions. The goal is to make it dead simple for a user to run through a guide and achieve some goal.

It is assumed that if you are following this template that you intend to write a guide for DataStax Astra. With that, we highly encourage you to download this markdown file and view it in both edit and rendered modes so you can easily see hidden comments.

If you'd like to see a working example of this guide [navigate here](https://astra.datastax.com/guide/astraPortalGuideTemplate) and login to Astra.

**In this guide, we will discuss**
- Creating your guide in Github
- How to format guides and create actions
- Configuring your guide
- What not to do 😬
- How to submit a guide

# Prerequisites
**If you don't have any prerequisite content just remove this section altogether.**

This section contains items that a user may need from outside of Astra. Examples are things like Maven for Java or installing Node or Python. 
- If any prereqs are required be explicit and call them out
- Provide links to needed resources
- Here is an example:
    - [Download](https://maven.apache.org/download.cgi) and [install](https://maven.apache.org/install.html) Maven.

Here's something for fun

![test image for fun](https://media.giphy.com/media/107QsHzZW54hJC/giphy.gif)
<!--
You can use inline links (install) or provide them later with a named reference (Download). Either is fine. Up to you.
 -->

<!-- 
For each section use ##, the number of the section itself, and the section title. These will automatically
be picked up by a preprocessor and used to properly style the guide. While you can generally use 
whatever markdown you want you don't need to worry about trying to match styles within Astra, we'll do that for you.
Notice the example below "## 1 How to get started".
 -->
## 1  Creating your guide in Github
### 1a Pick a name for your guide directory
Try to make this short and descriptive. 

Use **_camelCase_**, _meaning capitalize the first letter of each new word after the first word_. 

This will be the path used in Astra to access your guide.

Here are some examples:
- introToDataWithAstra
- overviewOfAstraDB
- astraDBApplicationQuickstartPython

### 1b Create a directory and your README.md file
Now that you have a directory name you can create it along with your README.md in Github. 

To do this, click the **_Add file_** drop down in the top right hand corner and choose the **_Create new file_** option within this repo. This will bring you to a page like you see in the image below.

<img alt="Create directory and readme" src="https://github.com/riptano/astra-portal-getting-started/blob/main/createDirectoryAndReadme.png?raw=true" width="100%" />

Here, you will both name your guide directory and create a README.md file to work from.

Start off by typing the **_name of the directory for your guide_** in the field provided. Then, type a slash character **_"/"_** right after the directory name and add **_README.md_**. 

So in the example above, we typed **_"yourDirectory/README.md"_** directly in the field provided.

### 1c Add text to README.md
If you already have some text for your **_README.md_** file can you paste it directly into the field provided. 

_Note the example "**Put things here in the README.md file**" in the image above._

_Also, don't worry if you don't have all of your text ready, you can always edit more later._

### 1d Create a branch
Ok, now we're ready to create a branch.

To do this, scroll down to the bottom of the page from the previous step.

Click the **_Create a new branch and start a pull request_** radio button.

Fill out the branch name in the field provided. Github should automatically fill in your username. Just add your directory name and the word **_"guide"_** separated by dashses (for example: **_SonicDMG-yourDirectory-guide_**) as you see in the image below.

<img alt="Create guide branch" src="https://github.com/riptano/astra-portal-getting-started/blob/main/createGuideBranch.png?raw=true" width="100%" />

Then click **_Propose new file_**.

### 1e Create a draft pull request
Now that you have a branch you should see a screen like the one below.

<img alt="Draft pull request" src="https://github.com/riptano/astra-portal-getting-started/blob/main/draftPR.png?raw=true" width="100%" />

Click the **_...pull request_** dropdown on the lower right hand corner.

Choose the **_Create draft pull request_** option. The button will change to **_Draft pull request_**.

Now click this button to create a draft pull request. _A draft pull request means you are still making edits and it's not ready for review._

### 1f Navigate to your README.md and edit
Finally, we need to get to your newly created **_README.md_** and open it for editing. 

Look at the image below. 

You should see a link to the branch you just created.

Click this link. This will bring you directly to your newly created branch within Github.

<img alt="Navigate to readme" src="https://github.com/riptano/astra-portal-getting-started/blob/main/navigateToReadme.png?raw=true" width="100%" />

Now click on the new directory you added previously.

<img alt="Navigate to directory" src="https://github.com/riptano/astra-portal-getting-started/blob/main/navigateToDirectory.png?raw=true" width="100%" />

**_README.md_** should be selected by default. Click on the **_edit_** (_pencil_) icon on the top right to start editing.

<img alt="Edit readme" src="https://github.com/riptano/astra-portal-getting-started/blob/main/editReadme.png?raw=true" width="100%" />

Once you're done with your edits, scroll down to the bottom of the page and **_commit_** your changes to your branch.

_Note: Once you have a draft PR in place you can continue to make changes as needed._ 

Follow the sections below to learn how to format your guide. Once complete, the last step (5) will explain how to submit your PR for final review.

## 2 How to format guides and create actions
Generally, formatting is pretty open and follows normal markdown styles. The main caveats being guide metadata in the overview, using numbered sections for proper styling within Astra, and using **actions**.

### Uhhh, what are actions?
Glad you asked. **Actions** are special options that allow you to easily bring a user through a set of Astra specific operations with a simple button click. The goal is to remove friction from the user experience and make it easier for guide creators to add in more complex operations.

An example is database creation. If you want a user to create a database then use ```<<createDatabase>>``` directly in markdown. Again, use **_edit_** mode to see a real example.
<<createDatabase>>

If you've done this correctly in markdown you'll only see the rendered action. Within an Astra guide this will translate into a fully operational button or link with status updates and other functionality. 

_**Note:** **Actions** will potentially bring users into a new flow to complete the **action**, but will then bring users back to the guide once exited._

### Currently available **_actions_** _(these will only render within Astra)_
```<<createDatabase>>```

<<createDatabase>>

```<<createVectorDatabase>>```

<<createVectorDatabase>>

```<<createToken>>```

<<createToken>>

```<<launchCQLConsole>>```

<<launchCQLConsole>>

```<<downloadSCB>>```

<<downloadSCB>>

```<<launchDataLoader>>```

<<launchDataLoader>>

## 3 Configuring your guide
Ok, so now you've got the basics down and have some content. Great, before you submit, there's one more thing for you to do. You must configure your guide.

### Metadata
Each guide will have it's own section within the config.json. The metadata for THIS guide template looks like this.
```json
"astraPortalGuideTemplate": {
  "locale": "en-us",
  "title": "Astra Portal Getting Started TEMPLATE 🎇",
  "description": "Get an overview of how to write 'getting started' guides for DataStax Astra.",
  "skillLevel": "Beginner",
  "timeToComplete": "10 minutes",
  "recommendedLinks": [{
    "url": "https://www.freecodecamp.org/news/how-to-create-a-local-git-branch/",
    "text": "How to create branches in Git"
  }, {
    "url": "https://github.com/markdown-templates/markdown-emojis",
    "text": "All the markdown emojis"
  }],
  "recommendedGuides": [
    "overviewOfAstraDB"
  ],
  "contentSrc": "astraPortalGuideTemplate/README.md",
  "stepCount": 6
}
```

Again, just use this one as an example for your own guide.

### Breaking it down
Ok, let's break each property down to see what they do.

#### Guide name **_and_** route
This one is important. Not only is it the unique name given to your guide, but it determines the route to the guide within Astra. **Case matters!** 

```json
"astraPortalGuideTemplate": {
```
By setting this property the route in Astra will be "https://astra.datastax.com/guide/astraPortalGuideTemplate"

#### Guide details
The guide detail section will give users high level information about your guide. Things like the `title`, a short `description`, `skill level`, and approx. `time to complete`.

The `title` should conform to **20** chars min, **73** chars max.

The `description` should conform to **40** chars min, **110** chars max.
```json
"locale": "en-us", // just use this value for now
"title": "Astra Portal Getting Started TEMPLATE 🎇, but I need more to hit 73 chars🚀",
"description": "Get an overview of how to write 'getting started' guides for DataStax Astra and then keep going to 110 chars.🌈",
"skillLevel": "Beginner",
"timeToComplete": "10 minutes",
```
Each of these values will then be automatically rendered within Astra, both in the title cards displayed on the home page and within the guides themselves.

#### Recommended Links
While you may include inline links for content, guides also include explicit resource call outs in the right-hand side navigation. These are for links you really want to bring attention to and should be constrained to just a few links at most. 

The example below contains two links that will be displayed under the auto-generated table of contents to the right.
```json
"recommendedLinks": [{
  "url": "https://www.freecodecamp.org/news/how-to-create-a-local-git-branch/",
  "text": "How to create branches in Git"
}, {
  "url": "https://github.com/markdown-templates/markdown-emojis",
  "text": "All the markdown emojis"
}],
```

#### Recommended guides
If your guide is part of a larger set or you want to point users to a different guide upon completion of your guide use the "recommendedGuides" property to do this. Similar to recommended links you can provide multiple guides if you wise. 

Values you use within the `recommendGuides` section **MUST MATCH** guide names from the config.json **EXACTLY**.

```json
"recommendedGuides": [
  "overviewOfAstraDB", "introToDataWithAstraDB"
],
```

#### Source and step count
Finally, we come to the `contentSrc` and `stepCount` properties. 

The `contentSrc` property tells the guide renderer where in the repository your guide exists. If this value is incorrect your guide will not render. 

The `stepCount` property tells the renderer how many steps you have in your guide. For example, this guide has six steps ending with "6 How to submit a guide". So, the `stepCount` in this case should be "6". The renderer will do the rest and auto-generate the table of contents and all that.
```json
    "contentSrc": "astraPortalGuideTemplate/README.md",
    "stepCount": 6
}
```
## 4 What not to do 😬
We ask that you don't include artifacts that go stale, like UI screenshots that change over time. Our goal is to provide guides that are as maintenance free as possible for both you and our users. Nothing like using a guide that was great a year ago only to find out nothing in it works halfway through.

## 5 How to submit a guide
Ok great, your guide is ready and now you want to submit a pull request (PR) to get it published. All we need to do is mark your draft pull request "Ready for review" in the **_Pull requests_** tab in Github. 

Click the **_Pull requests_** tab.

Click on your pull request.

Click the **_Ready for review_** button.

That's it! At this point one of the review team will be notified to start reviewing your request. Awesome job!