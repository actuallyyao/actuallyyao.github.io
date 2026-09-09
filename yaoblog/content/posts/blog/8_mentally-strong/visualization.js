// Define the data for the bar chart
const data = [4, 8, 15, 16, 23, 42];

// Define the dimensions of the chart
const margin = { top: 20, right: 30, bottom: 30, left: 40 };
const width = 960 - margin.left - margin.right;
const height = 500 - margin.top - margin.bottom;

// Create an SVG element to contain the chart
const svg = d3
  .select('#chart-container')
  .append('svg')
  .attr('width', width + margin.left + margin.right)
  .attr('height', height + margin.top + margin.bottom)
  .append('g')
  .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

// Define the x and y scales for the chart
const x = d3.scaleBand().range([0, width]).padding(0.1);
const y = d3.scaleLinear().range([height, 0]);

x.domain(data.map((d, i) => i));
y.domain([0, d3.max(data)]);

// Add the bars to the chart
svg
  .selectAll('.bar')
  .data(data)
  .enter()
  .append('rect')
  .attr('class', 'bar')
  .attr('x', (d, i) => x(i))
  .attr('width', x.bandwidth())
  .attr('y', (d) => y(d))
  .attr('height', (d) => height - y(d));

// Add the x and y axis to the chart
svg
  .append('g')
  .attr('transform', 'translate(0,' + height + ')')
  .call(d3.axisBottom(x));
svg.append('g').call(d3.axisLeft(y));