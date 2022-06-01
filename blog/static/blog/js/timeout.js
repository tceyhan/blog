let element = document.querySelector('.alert');

setTimeout(function () {
  element.style.display = 'none';
}, 3000);

let like = document.querySelector('.like');

like.addEventListener('click', () => {
  console.log("likeeee")
  // let likeCount = document.getElementById('likeCount');
  // let count = parseInt(likeCount.innerHTML);
  // likeCount.innerHTML = count + 1; 
  
});