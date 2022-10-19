importAll(r) {
  let images = {};
  r.keys().map((item, index) => { images[item.replace('./', '')] = r(item); });
  return images;
}

const images=importAll(require.context('../IMG', false, /\.(png|jpe?g|svg)$/));

< img src={images['color-choice1.jpg']} />
  
