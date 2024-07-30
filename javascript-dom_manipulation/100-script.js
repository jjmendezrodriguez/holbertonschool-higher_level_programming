document.addEventListener('DOMContentLoaded', () => {
    const myList = document.querySelector('.my_list');
    const addItemDiv = document.getElementById('add_item');
    const removeItemDiv = document.getElementById('remove_item');
    const clearListDiv = document.getElementById('clear_list');
  
    addItemDiv.style.cssText = "cursor: pointer; padding: 10px; border: 1px solid black; display: inline-block; margin: 5px; background-color: lightgray;";
    removeItemDiv.style.cssText = "cursor: pointer; padding: 10px; border: 1px solid black; display: inline-block; margin: 5px; background-color: lightgray;";
    clearListDiv.style.cssText = "cursor: pointer; padding: 10px; border: 1px solid black; display: inline-block; margin: 5px; background-color: lightgray;";

    // Agregar un nuevo elemento a la lista
    addItemDiv.addEventListener('click', () => {
      const newItem = document.createElement('li');
      newItem.textContent = 'Item';
      myList.appendChild(newItem);
    });
  
    // Eliminar el último elemento de la lista
    removeItemDiv.addEventListener('click', () => {
      const lastItem = myList.lastElementChild;
      if (lastItem) {
        myList.removeChild(lastItem);
      }
    });
  
    // Limpiar todos los elementos de la lista
    clearListDiv.addEventListener('click', () => {
      while (myList.firstChild) {
        myList.removeChild(myList.firstChild);
      }
    });
  });
  