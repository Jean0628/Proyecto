'use strict';



/**
 * add event on element
 */

const addEventOnElem = function (elem, type, callback) {
  if (elem.length > 1) {
    for (let i = 0; i < elem.length; i++) {
      elem[i].addEventListener(type, callback);
    }
  } else {
    elem.addEventListener(type, callback);
  }
}



/**
 * navbar toggle
 */

const navbar = document.querySelector("[data-navbar]");
const navToggler = document.querySelector("[data-nav-toggler]");
const navLinks = document.querySelectorAll("[data-nav-link]");

const toggleNavbar = () => navbar.classList.toggle("active");

addEventOnElem(navToggler, "click", toggleNavbar);

const closeNavbar = () => navbar.classList.remove("active");

addEventOnElem(navLinks, "click", closeNavbar);



/**
 * header & back top btn active when scroll down to 100px
 */

const header = document.querySelector("[data-header]");
const backTopBtn = document.querySelector("[data-back-top-btn]");

const headerActive = function () {
  if (window.scrollY > 100) {
    header.classList.add("active");
    backTopBtn.classList.add("active");
  } else {
    header.classList.remove("active");
    backTopBtn.classList.remove("active");
  }
}

addEventOnElem(window, "scroll", headerActive);



/**
 * filter function
 */

const filterBtns = document.querySelectorAll("[data-filter-btn]");
const filterItems = document.querySelectorAll("[data-filter]");

let lastClickedFilterBtn = filterBtns[0];

const filter = function () {
  lastClickedFilterBtn.classList.remove("active");
  this.classList.add("active");
  lastClickedFilterBtn = this;

  for (let i = 0; i < filterItems.length; i++) {
    if (this.dataset.filterBtn === filterItems[i].dataset.filter ||
      this.dataset.filterBtn === "all") {

      filterItems[i].style.display = "block";
      filterItems[i].classList.add("active");

    } else {

      filterItems[i].style.display = "none";
      filterItems[i].classList.remove("active");

    }
  }
}

addEventOnElem(filterBtns, "click", filter);








// Registro de horas seleccionadas para cada día y barbero
var horasPorBarberoYDia = {};

// Función para actualizar las fechas disponibles según el barbero seleccionado
function actualizarFechasDisponibles() {
  var fechaInput = document.getElementById("fechaInput");
  var barberoSelect = document.getElementById("barbero");

  // Obtener el barbero seleccionado
  var barberoSeleccionado = barberoSelect.value;

  // Restaurar la lista completa de fechas disponibles para el barbero seleccionado
  fechaInput.innerHTML = "";

  // Agregar todas las fechas disponibles
  var todasLasFechas = Object.keys(horasPorBarberoYDia[barberoSeleccionado] || {});

  todasLasFechas.forEach(function (fecha) {
    var option = document.createElement("option");
    option.value = fecha;
    option.text = fecha;
    fechaInput.add(option);
  });

  // Llamar a la función para actualizar las horas después de seleccionar la fecha
  actualizarHorasDisponibles();
}

// Función para actualizar las horas disponibles según el día seleccionado
function actualizarHorasDisponibles() {
  var fechaInput = document.getElementById("fechaInput");
  var horaSelect = document.getElementById("horaSelect");

  // Obtener la fecha seleccionada
  var fechaSeleccionada = fechaInput.value;

  // Obtener el barbero seleccionado
  var barberoSelect = document.getElementById("barbero");
  var barberoSeleccionado = barberoSelect.value;

  // Restaurar la lista completa de horas disponibles para el día seleccionado y barbero
  horaSelect.innerHTML = "<option value='Select category'>Selecciona la hora</option>";

  // Agregar todas las horas disponibles
  var todasLasHoras = ["8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM"];

  // Filtrar las horas ya seleccionadas para la fecha seleccionada y barbero
  var horasSeleccionadas = horasPorBarberoYDia[barberoSeleccionado]?.[fechaSeleccionada] || [];

  todasLasHoras.forEach(function (hora) {
    if (!horasSeleccionadas.includes(hora)) {
      var option = document.createElement("option");
      option.value = hora;
      option.text = hora;
      horaSelect.add(option);
    }
  });
}

// Función para seleccionar y quitar la hora
function seleccionarYQuitarHora() {
  var fechaInput = document.getElementById("fechaInput");
  var horaSelect = document.getElementById("horaSelect");
  var horaSeleccionada = horaSelect.value;
  var fechaSeleccionada = fechaInput.value;
  var barberoSelect = document.getElementById("barbero");
  var barberoSeleccionado = barberoSelect.value;

  if (horaSeleccionada !== "Select category") {
    alert("Has seleccionado la hora: " + horaSeleccionada);

    // Agregar la hora seleccionada al registro para el día y barbero seleccionados
    if (!horasPorBarberoYDia.hasOwnProperty(barberoSeleccionado)) {
      horasPorBarberoYDia[barberoSeleccionado] = {};
    }

    if (!horasPorBarberoYDia[barberoSeleccionado].hasOwnProperty(fechaSeleccionada)) {
      horasPorBarberoYDia[barberoSeleccionado][fechaSeleccionada] = [];
    }

    horasPorBarberoYDia[barberoSeleccionado][fechaSeleccionada].push(horaSeleccionada);

    // Quitar la hora seleccionada del select
    horaSelect.remove(horaSelect.selectedIndex);

    // Restaurar la opción predeterminada
    var opcionPredeterminada = document.createElement("option");
    opcionPredeterminada.value = "Select category";
    opcionPredeterminada.text = "Selecciona la hora";
    horaSelect.add(opcionPredeterminada);

    // Limpiar los demás campos del formulario
    document.getElementById("citaForm").reset();

    // Actualizar las fechas y horas disponibles después de la selección
    actualizarFechasDisponibles();
  }
}

