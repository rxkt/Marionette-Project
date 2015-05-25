function Bar() {

    var Data = [{
	'x': 1, //FIll it in with Data from Mongo though socket later
	'y': 1
    }, {
	'x': 2,
	'y': 2
    }];

    var chart = d3.select('#visualisation'),
    WIDTH = 500,
    HEIGHT = 500,
    MARGINS = {
	top: 10,
	right: 10,
	bottom: 10,
	left: 10
    },
    xRange = d3.scale.ordinal().rangeRoundBands([MARGINS.left, WIDTH - MARGINS.right]).domain([d3.min(Data, function(d) {
	return d.x;
    }), d3.max(Data, function(d) {
	return d.x;
    })]),										   
    yRange = d3.scale.ordinal().rangeRoundBands([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([d3.min(Data, function(d) {
	return d.y;
    }), d3.max(Data, function(d) {
	return d.y;
    })]),
    xAxis = d3.svg.axis()
    .scale(xRange)
    .tickSize(5)
    .tickSUbdivide(true);,
    yAxis = d3.svg.axis()
    .scale(yRange)
    .tickSize(5)
    .orient('left')
    .tickSUbdivide(true);
    
Chart.append('svg:g')
  .attr('class', 'x axis')
  .attr('transform', 'translate(0,' + (HEIGHT - MARGINS.bottom) + ')')
  .call(xAxis);
 
Chart.append('svg:g')
  .attr('class', 'y axis')
  .attr('transform', 'translate(' + (MARGINS.left) + ',0)')
  .call(yAxis);

Chart.selectAll('rect')
  .data(Data)
  .enter()
  .append('rect')
  .attr('x', function(d) {
    return xRange(d.x);
  })
  .attr('y', function(d) {
    return yRange(d.y);
  })
  .attr('width', xRange.rangeBand()) 
  .attr('height', function(d) {     
    return ((HEIGHT - MARGINS.bottom) - yRange(d.y));
  })
  .attr('fill', 'grey');  
};

Bar();
