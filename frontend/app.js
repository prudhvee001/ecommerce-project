fetch('http://localhost:3002/products')
  .then(response => response.json())
  .then(products => {
    const productList = document.getElementById('product-list');
    products.forEach(product => {
      const productDiv = document.createElement('div');
      productDiv.textContent = `${product.name} - $${product.price}`;
      productList.appendChild(productDiv);
    });
  });
