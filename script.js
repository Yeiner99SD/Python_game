let nums = [8, 4, 6, 3, 1];
let target = 9;

for (let i = 0; i < nums.length; i++) { // Itera sobre cada índice
  for (let j = i + 1; j < nums.length; j++) { // Segundo índice comienza desde el siguiente al índice actual
    let control = nums[i] + nums[j]; // Calcula la suma

    if (control == target) { // Verifica si la suma es igual al target
      document.write(i, ' ,', j); // Imprime los índices si la suma es igual al target
    }
  }
}



