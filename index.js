import config from './config.json'
const context = require.context('./', true, /\.md$/);
const all = {};
context.keys().forEach((key) => {
  if (key.includes("@riptano")) {
    return;
  }
  const fileName = key.replace('./', '');
  const resource = require(`./${fileName}`);
  all[fileName] = resource;
});

export {
    config,
    all
}