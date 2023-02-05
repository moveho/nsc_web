function setChart() {
  Highcharts.setOption({
    global: {
      useUTC: false
    }
  });
};

$.ajax({
  url: "{% url 'stockapp:kospiview' %}",
  dataType: 'json',
  success: function (data) {

    Highcharts.setOptions({
      global: {
        useUTC: false
      }
    });

    Highcharts.stockChart("container", {

      chart: {
        height: 500
      },

      title: {
        text: '코스피 지수'
      },

      rangeSelector: {
        selected: 5,
        inputEnabled: false
      },

      xAxis: {
        type: 'datetime',
        labels:{
          formatter: function(){
            return Highcharts.dateFormat('%y.%m.%d', this.value);
          },
          step: 3
        }
      },

      yAxis: {
        labels: {
          format: '{value}p',
          style: {
            color: 'rgba(0,0,0,.6)',
          },
          x: 30,
        },
        opposite: false,
        tickInterval: 50,
      },

      tooltip: {
        xDateFormat: '%Y-%m-%d',
        split: true
      },

      series: [{
          name: '시가',
          data: data.open,
          color: 'rgba(0,200,0,.6)',
          lineWidth: 2
      },
      {
          name: '종가',
          data: data.close,
          lineWidth: 3
      }],

      legend: {
        enabled: true,
        align: 'left',
        verticalAlign: 'top',
        floating: true,
        x: 30,
        y: 70
      },

      responsive: {
        rules: [{
          condition: {
            maxWidth: 600
          },
          chartOptions: {
            chart: {
              height: 300
            },
            navigator: {
              enabled: false
            }
          }
        }]
      }
    });
  }
});