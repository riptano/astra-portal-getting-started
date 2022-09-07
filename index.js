import config from './config.json'
let context;
if (!require.context || typeof require.context === "undefined" ) {
  context = {}
} else {
  context = require.context('./', true, /\.md$/);
}

const all = {};
if (context.keys) {
  context.keys().forEach((key) => {
    if (key.includes("@riptano")) {
      return;
    }
    const fileName = key.replace('./', '');
    const resource = require(`./${fileName}`);
    all[fileName] = resource;
  });
}


export {
    config,
    all
}