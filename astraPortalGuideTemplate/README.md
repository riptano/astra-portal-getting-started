<!-- 
This is the overview section. 
The overview should provide users a high level explanation of what your guide is all about at a glance. 
What will they learn, what will they get out of it?
 -->
# Overview
Hiya. Welcome to the Astra getting started guide template. Use this template to help "guide" you through authoring "getting started" guides within DataStax Astra. 😏

"Getting Started" guides are a unique way to help Astra users learn about a topic or how to perform a set of actions. The goal is to make it dead simple for a user to run through a guide and achieve some goal.

It is assumed that if you are following this template that you intend to write a guide for DataStax Astra. With that, we highly encourage you to donwload this markdown file and view it in both edit and rendered modes so you can easily see hidden comments.

Feel free to copy this readme.md in its entirety and use within your guide to get started.

**In this guide, we will discuss**
- How to get started
- Where to put your guide
- How to format guides and create actions
- Configuring your guide
- What NOT to do 😬
- How to submit a guide

**Prerequisites**

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
## 1  How to get started
### Download the repo locally
You'll be submitting a pull request for your content so you'll want to download this repo locally so you can easily create, iterate on, and commit changes.

If you haven't already, ensure you view this markdown in **EDIT** mode to get instructions for each section.

<!-- 
Notice the code blocks in the following section. These are completely valid to use within guides.
 -->
### Create a branch
You'll need to create a branch to submit your pull request. Use the following command, **replacing the branch name**, for something unique to your guide.
```shell
git checkout -b yourbranchnamehere
```

The above command should have auto switched to your new branch. Let's check anyway just to be sure.
```shell
git branch
```

## 2  Where to put your guide
### Create a folder in the repo to contain guide contents
Ensure you create your guide folder with something identifiable. For example, we could use something like "/astraPortalGuideTemplate" for this guide. It's pretty open. We just ask you not use something like "/guide" that's overly generic.

### Copy **THIS** readme.md
Make a copy of **THIS** readme.md to use in your own guide as a starting point and store in your newly created folder.

## 3 How to format guides and create actions
Generally, formatting is pretty open and follows normal markdown styles. The main caveats being guide metadata in the overview, using numbered sections for proper styling within Astra, and using **actions**.

### Uhhh, what are actions?
Glad you asked. **Actions** are special options that allow you to easily bring a user through a set of Astra specific operations with a simple button click. The goal is to remove friction from the user experience and make it easier for guide creators to add in more complex operations.

An example is database creation. If you want a user to create a database then use ```<<createDatabase>>``` directly in markdown. Again, use **EDIT** mode to see a real example.
<<createDatabase>>

If you've done this correctly in markdown you'll only see the rendered action. Within an Astra guide this will translate into a fully operational button or link with status updates and other functionality. **NOTE** that **actions** will potentially bring users into a new flow to complete the **action**, but will then bring users back to the guide once exited.

### Currently available **ACTIONS** _(these will only render within Astra)_
```<<createDatabase>>```

<<createDatabase>>

```<<createToken>>```

<<createToken>>

```<<launchCQLConsole>>```

<<launchCQLConsole>>

```<<downloadSCB>>```

<<downloadSCB>>

```<<launchDataLoader>>```

<<launchDataLoader>>

## 4 Configuring your guide
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

#### Guide name AND route
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
"title": "Astra Portal Getting Started TEMPLATE 🎇",
"description": "Get an overview of how to write 'getting started' guides for DataStax Astra.",
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
## 5 What NOT to do 😬
We ask that you don't include artifacts that go stale, like UI screenshots that change over time. Our goal is to provide guides that are as maintenance free as possible for both you and our users. Nothing like using a guide that was great a year ago only to find out nothing in it works halfway through.

## 6 How to submit a guide
```shell
git push --set-upstream origin yourbranchnamehere
```