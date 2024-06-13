 
use <Anton-Regular.ttf>

// Constants
font = "Anton-Regular";
default_thickness = 1.5;
default_height = 180;
default_width = 15;
label_color = "DimGray";

// Garden Label Module
module GardenLabel(txt, thickness = default_thickness, height = default_height, width = default_width, font = font) {
	// Triangle Module
	module triangle(p) {
		x = p[0];
		y = p[1];
		h = p[2];
		translate([0, 0, h]) {
			polygon([[0, 0], [x, 0], [x/2, y]]);
		}
	}

	// Label Text Module
	module LabelText(txt, width, font) {
		rotate([0, 0, -90]) {
			text(txt, size = width + 2, font = font);
		}
	}
	
	// Base
	color(label_color)
	linear_extrude(thickness) {
		union() {
			triangle([width, -width, width]);
			square([width, height]);
			translate([0, height, 0]) LabelText(txt, width, font);
		}
	}
	
	// Label Text
	translate([0, height, thickness]) {
		linear_extrude(1) LabelText(txt, width, font);
	}
}

// Example
GardenLabel("Potato");