      const currentLocation = window.location;

      if (currentLocation.toString().includes("dashboard")) {
        const item = document.querySelector("#dashboard-item");
        const link = document.querySelector("#dashboard-link");
        const icon = document.querySelector("#dashboard-icon");
        const arrow = document.querySelector("#dashboard-arrow-icon");

        item.classList.add("nav-item-active");
        link.classList.add("nav-link-active");
        icon.classList.add("icon-active");
        arrow.classList.remove("icon-inactive");
        arrow.classList.add("icon-active");
      }

      if (currentLocation.toString().includes("clients")) {
        const item = document.querySelector("#clients-item");
        const link = document.querySelector("#clients-link");
        const icon = document.querySelector("#clients-icon");
        const arrow = document.querySelector("#clients-arrow-icon");

        item.classList.add("nav-item-active");
        link.classList.add("nav-link-active");
        icon.classList.add("icon-active");
        arrow.classList.remove("icon-inactive");
        arrow.classList.add("icon-active");
      }

      if (currentLocation.toString().includes("purchases")) {
        const item = document.querySelector("#purchases-item");
        const link = document.querySelector("#purchases-link");
        const icon = document.querySelector("#purchases-icon");
        const arrow = document.querySelector("#purchases-arrow-icon");

        item.classList.add("nav-item-active");
        link.classList.add("nav-link-active");
        icon.classList.add("icon-active");
        arrow.classList.remove("icon-inactive");
        arrow.classList.add("icon-active");
      }

      if (currentLocation.toString().includes("payments")) {
        const item = document.querySelector("#payments-item");
        const link = document.querySelector("#payments-link");
        const icon = document.querySelector("#payments-icon");
        const arrow = document.querySelector("#payments-arrow-icon");

        item.classList.add("nav-item-active");
        link.classList.add("nav-link-active");
        icon.classList.add("icon-active");
        arrow.classList.remove("icon-inactive");
        arrow.classList.add("icon-active");
      }