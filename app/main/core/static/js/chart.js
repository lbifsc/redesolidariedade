const options = {
  chart: {
    height: 450,
    width: 400,
    type: "line",
    background: "#fff",
    foreColor: "#333",
    offsetY: -10,
  },
  colors: ["#000"],
  series: [
    {
      name: "Sales",
      data: [30, 40, 35, 50, 49, 60, 70, 91, 125],
    },
  ],
  xaxis: {
    categories: [1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999],
  },
  grid: {
    padding: {
      top: 40,
      right: 40,
      bottom: 10,
      left: 1,
    },
  },
};

const chart = new ApexCharts(document.querySelector("#chart"), options);

chart.render();
