$(function() {
    firebasetempRef = firebase.database().ref().child("temp");
    class GaugeChart {
        constructor(element, params) {
            this._element = element;
            this._initialValue = params.initialValue;
            this._higherValue = params.higherValue;
            this._title = params.title;
            this._subtitle = params.subtitle;
        }

        _buildConfig() {
            let element = this._element;

            return {
                value: this._initialValue,
                valueIndicator: {
                    color: '#fff'
                },

                geometry: {
                    startAngle: 180,
                    endAngle: 360
                },

                scale: {
                    startValue: 0,
                    endValue: this._higherValue,
                    customTicks: [0, 20, 40, 60, 80, 100, 120],
                    tick: {
                        length: 8
                    },

                    label: {
                        font: {
                            color: '#87959f',
                            size: 9,
                            family: '"Open Sans", sans-serif'
                        }
                    }
                },



                title: {
                    verticalAlignment: 'bottom',
                    text: this._title,
                    font: {
                        family: '"Open Sans", sans-serif',
                        color: '#fff',
                        size: 10
                    },

                    subtitle: {
                        text: this._subtitle,
                        font: {
                            family: '"Open Sans", sans-serif',
                            color: '#fff',
                            weight: 700,
                            size: 28
                        }
                    }
                },



                onInitialized: function() {
                    let currentGauge = $(element);
                    let circle = currentGauge.find('.dxg-spindle-hole').clone();
                    let border = currentGauge.find('.dxg-spindle-border').clone();

                    currentGauge.find('.dxg-title text').first().attr('y', 48);
                    currentGauge.find('.dxg-title text').last().attr('y', 28);
                    currentGauge.find('.dxg-value-indicator').append(border, circle);
                }
            };


        }

        init() {
            $(this._element).dxCircularGauge(this._buildConfig());
        }
    }

    firebasetempRef.on('value', function(datasnapshot) {



        $(document).ready(function() {

            $('.gauge').each(function(index, item) {
                let params = {
                    initialValue: datasnapshot.val(),
                    higherValue: 120,
                    title: `Temperature ºC`,
                    subtitle: datasnapshot.val()

                };


                let gauge = new GaugeChart(item, params);
                gauge.init();
            });

        });
    });




});