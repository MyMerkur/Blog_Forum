//TR
window.onload = async function () {
  const OriginalData = await fetch("static/json/data.json");
  const TransferedData = await OriginalData.json();
  let siteMain = document.querySelector(".siteMain");
  TransferedData.forEach((item, index) => {
    let card = document.createElement("div");
    card.classList.add("card");
    card.classList.add("cardContainer");
    card.id = `card-${index + 1}`;


    let cardOverlay = document.createElement("div");
    cardOverlay.classList.add("card-img-overlay");

    let h4 = document.createElement("h4");
    h4.classList.add("card-text");
    h4.textContent = item.content;

    let img = document.createElement("img");
    img.classList.add("card-img");
    img.src = item.src;
    img.alt = item.id;

    cardOverlay.appendChild(h4);

    card.appendChild(img);
    card.appendChild(cardOverlay);

    siteMain.appendChild(card);


    //Programing Language Scroll Effect
    window.addEventListener("scroll", function () {
      const scrollY = window.scrollY;
      const cards = [
        { id: "card-1", threshold: 300 },
        { id: "card-2", threshold: 600 },
        { id: "card-3", threshold: 900 },
        { id: "card-4", threshold: 1200 },
        { id: "card-5", threshold: 1500 },
        { id: "card-6", threshold: 1600 },
      ];

      cards.forEach((cardData) => {
        const card = document.querySelector(`#${cardData.id}`);
        if (scrollY > cardData.threshold) {
          card.style.opacity = 1;
        } else {
          card.style.opacity = 0;

        }
      });
    });

    window.addEventListener("scroll", function () {
      let arrowDown = this.document.querySelector("#arrowDown");
      const scrollY = window.scrollY;

      if (scrollY > 300) {
        arrowDown.style.display = "none"
      } else {
        arrowDown.style.display = "block"

      }

    });

    window.addEventListener("scroll", function () {
      let upBtn = this.document.querySelector(".upBtn");
      const scrollY = window.scrollY;

      if (scrollY > 1200) {
        upBtn.style.display = "block"
      } else {
        upBtn.style.display = "none"
      }

      upBtn.addEventListener("click", function () {
        window.scrollTo({
          top: 0,
          behavior: "smooth"
        })
      })
    })

    //parantez bitişi
  });
};

//Page Scroll Change 
window.addEventListener("scroll", function () {
  let navigatorBar = document.querySelector(".navigation-bar");
  let responsiveNavigatorBar = document.querySelector(".responsiveNavigatorBar");
  const scrollY = window.scrollY;

  if (scrollY > 250) {
    navigatorBar.style.opacity = "0";
    responsiveNavigatorBar.style.display = "flex"
    responsiveNavigatorBar.style.opacity = "1";
  } else {
    navigatorBar.style.opacity = "1";
    responsiveNavigatorBar.style.display = "none"
    responsiveNavigatorBar.style.opacity = "0";
  }
});


//Responsive Menu Open-Close
let navigatorUl = document.querySelector("#navigatorUl");
let responsiveNavigatorBar = document.querySelector(".responsiveNavigatorBar")
responsiveNavigatorBar.addEventListener("click", function () {
  if (navigatorUl.style.opacity === "1") {
    navigatorUl.style.opacity = "0"
  } else {
    navigatorUl.style.opacity = "1"
  }
})


//Draggable
responsiveNavigatorBar.addEventListener("dragstart", function (event) {
  event.dataTransfer.effectAllowed = "copy";
  event.dataTransfer.setData("text/plain", "Bu öğe sürükleniyor");
});

document.addEventListener("dragover", function (event) {
  event.preventDefault();

  let newPositionX = event.clientX;
  let newPositionY = event.clientY;

  responsiveNavigatorBar.style.left = newPositionX + "px";
  responsiveNavigatorBar.style.top = newPositionY + "px";
});


//Language
document.addEventListener("DOMContentLoaded", function () {

  let tr = document.querySelector("#tr");
  let en = document.querySelector("#en");

  tr.addEventListener("click", () => {
    window.location.href = '../index.html';
  });

  en.addEventListener("click", () => {
    window.location.href = "eng-templates/indexEng.html";
  });
});

//Locale-Save
tr.addEventListener("click", () => {
  localStorage.setItem("selectedLanguage", "tr");
  window.location.href = '../index.html';
});


en.addEventListener("click", () => {
  localStorage.setItem("selectedLanguage", "eng");
  window.location.href = "eng-templates/indexEng.html";
});


//Text Hovered Color
const h4Elements = document.querySelectorAll(".siteContent h4");

h4Elements.forEach(h4Element => {
  const words = h4Element.textContent.split(" ");
  h4Element.innerHTML = "";

  words.forEach((word, index) => {
    const span = document.createElement("span");
    span.textContent = word;
    span.addEventListener("mouseenter", () => {
      span.style.color = "transparent";
      span.style.backgroundImage = "linear-gradient(45deg, #ff8a00, #e52e71)";
      span.style.backgroundClip = "text";
    });
    span.addEventListener("mouseleave", () => {
      span.style.color = "black";
    });


    if (index < words.length - 1) {
      const space = document.createElement("span");
      space.textContent = " ";
      h4Element.appendChild(space);
    }

    h4Element.appendChild(span);
  });
});


//Blog Comment

let commentBtns = document.querySelectorAll(".comment-button");

let commentForms = document.querySelectorAll(".comment_form");
commentBtns.forEach((commentBtn, index) => {
  commentBtn.addEventListener("click", () => {
    let commentForm = commentForms[index];

    if (commentForm.style.display === "block") {
      commentForm.style.display = "none";
    } else {
      commentForm.style.display = "block";
    }
  });
});

//Search Lane
let searchInput = document.getElementById("search");
let streamingContainer = document.querySelector(".streaming");
let allEntries = Array.from(streamingContainer.querySelectorAll(".streaming_new_message"));
searchInput.addEventListener("input", () => {
  let searchTerm = searchInput.value.toLowerCase();

  allEntries.forEach((entry) => {
    let content = entry.querySelector(".user_text").textContent.toLowerCase();

    if (!content.includes(searchTerm)) {
      entry.style.display = "none";
    } else {
      entry.style.display = "block";
    }
  });
});


