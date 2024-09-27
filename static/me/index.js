function init_chart(history) {
  let points = 0;
  let data = history.map((x) => {
    points += x.delta;
    return { x: new Date(x.date).toLocaleString(), y: points };
  });

  data.push({ x: new Date().toLocaleString(), y: points });

  let element = document.querySelector("#chart");
  let chart = new ApexCharts(element, {
    series: [
      {
        name: "Reward Points",
        data,
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
  });
  chart.render();
}
