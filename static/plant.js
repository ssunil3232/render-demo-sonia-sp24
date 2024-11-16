const canvas = document.getElementById('plantCanvas');
const ctx = canvas.getContext('2d');

// Tree growth parameters
let trunkHeight = 0;
let leafRadius = 0;
let foliageOpacity = 0;

// Colors
const trunkColor = "#8B4513"; // Saddle brown
const leafColors = ["#32CD32", "#228B22", "#7CFC00", "#ADFF2F", "#006400"]; // Varied green shades

// Leaf positions (randomized but constrained to an ellipse)
const leaves = [];
const treeCenterX = canvas.width / 2; // Center X of the tree
const treeCenterY = canvas.height - 120; // Approx center Y of the canopy
const canopyRadiusX = 400; // Horizontal radius of the ellipse (wider)
const canopyRadiusY = 130; // Vertical radius of the ellipse (shorter)

function initializeLeaves() {
  for (let i = 0; i < 500; i++) { // Increase the number of leaves for dense coverage
    let angle = Math.random() * Math.PI * 2; // Random angle
    let distance = Math.sqrt(Math.random()); // Spread leaves evenly within the ellipse
    const offsetX = Math.cos(angle) * distance * canopyRadiusX; // X coordinate within ellipse
    const offsetY = Math.sin(angle) * distance * canopyRadiusY; // Y coordinate within ellipse
    const color = leafColors[Math.floor(Math.random() * leafColors.length)];
    leaves.push({ offsetX, offsetY, color, radius: 0 }); // Add initial leaf
  }
}

function drawTree() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw the trunk
  drawTrunk();

  // Draw leaves
  if (trunkHeight > 100) {
    drawFoliage();
  }
}

function drawTrunk() {
  ctx.fillStyle = trunkColor;

  // Tapered trunk
  ctx.beginPath();
  ctx.moveTo(canvas.width / 2 - 30, canvas.height); // Bottom left
  ctx.lineTo(canvas.width / 2 + 30, canvas.height); // Bottom right
  ctx.lineTo(canvas.width / 2 + 20, canvas.height - trunkHeight); // Top right
  ctx.lineTo(canvas.width / 2 - 20, canvas.height - trunkHeight); // Top left
  ctx.closePath();
  ctx.fill();
}

function drawFoliage() {
  leaves.forEach((leaf) => {
    ctx.fillStyle = leaf.color;
    ctx.globalAlpha = foliageOpacity;

    // Draw each leaf as a circle
    ctx.beginPath();
    ctx.arc(
      treeCenterX + leaf.offsetX, // X position relative to canopy center
      treeCenterY + leaf.offsetY - trunkHeight, // Y position relative to canopy center
      Math.min(leaf.radius, 25), // Limit max radius of each leaf
      0,
      Math.PI * 2
    );
    ctx.fill();

    // Gradually grow each leaf
    if (leaf.radius < 25) {
      leaf.radius += 0.5; // Increase size of each leaf
    }
  });

  ctx.globalAlpha = 1.0; // Reset alpha for other drawings
}

function animateTreeGrowth() {
  // Grow trunk
  if (trunkHeight < 180) {
    trunkHeight += 2;
  }

  // Increase foliage opacity as leaves grow
  if (trunkHeight > 100) {
    if (foliageOpacity < 1) {
      foliageOpacity += 0.02;
    }
  }

  drawTree();

  if (trunkHeight < 180 || foliageOpacity < 1 || leaves.some((leaf) => leaf.radius < 25)) {
    requestAnimationFrame(animateTreeGrowth);
  } else {
    // Fade in buttons after the tree animation is complete
    fadeInButtons();
  }
}

// Initialize leaves and start animation
initializeLeaves();
animateTreeGrowth();