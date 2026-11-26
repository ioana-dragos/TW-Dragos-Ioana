// Array cu imaginile din folderul ../MEDIA
const images: string[] = [
  "../MEDIA/images.jpg",
  "../MEDIA/logo.png",
  "../MEDIA/poza_login.webp"
];

// Obtinem elementul principal din DOM
const mainImage = document.getElementById("carousel-image") as HTMLImageElement;

// Verificam daca elementul exista
if (!mainImage) throw new Error("Elementul cu id-ul 'carousel-image' nu a fost gasit!");

let currentIndex = 0;

// Functie care schimba imaginea mare
function showNextImage() {
  currentIndex = (currentIndex + 1) % images.length;
  mainImage.src = images[currentIndex]!;
}

// Slider automat la 3 secunde
setInterval(showNextImage, 3000);