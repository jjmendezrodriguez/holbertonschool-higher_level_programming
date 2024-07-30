const myList = document.querySelector('.my_list');

const addItem = document.getElementById('add_item');

addItem.addEventListener('click', () => {
  const newItem = document.createElement('li');
  newItem.textContent = 'Item';
  myList.appendChild(newItem);
});