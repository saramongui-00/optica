const toJson = (objeto) => {
  return JSON.stringify(objeto);
};

const fromJson = (json) => {
  return JSON.parse(json);
};

module.exports = { toJson, fromJson };