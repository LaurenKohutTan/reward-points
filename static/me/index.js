let options = {
  series: [
    {
      name: "Reward Points",
      data: [
        { x: "6/11/2023", y: 10 },
        { x: "6/15/2023", y: 5 },
        { x: "6/18/2023", y: 3 },
        { x: "6/20/2023", y: 8 },
        { x: "7/12/2023", y: 0 },
      ],
    },
  ],
  chart: {
    toolbar: {
      show: false,
    },
    foreColor: "#FFFFFF",
    type: "line",
    height: 350,
  },
  stroke: {
    curve: "stepline",
  },
  dataLabels: {
    enabled: false,
  },
  markers: {
    hover: {
      sizeOffset: 4,
    },
  },
};

let chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
