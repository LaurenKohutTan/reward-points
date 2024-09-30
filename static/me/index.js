function init_chart(history) {
  let points = 0;
  let net_gain = 0;
  let data = history.map((x) => {
    points += x.delta;
    if (x.delta > 0) net_gain += x.delta;
    return { x: new Date(x.date), y: points };
  });

  data.push({ x: new Date(), y: points });

  let element = document.querySelector("#chart");
  let chart = new ApexCharts(element, {
    series: [
      {
        name: "Reward Points",
        data,
      },
    ],
    xaxis: {
      type: "datetime",
    },
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

  return net_gain;
}
