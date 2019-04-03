package fractal;

import fractal.Turtle;

import java.awt.*;
import java.awt.geom.*;

/**
 * A class that implements some basic fractal drawing methods using recursion.
 * These methods include the Koch curve, tree, Sierpinski triangle and carpet.
 */
public class Fractal {
	private Graphics2D g2d = null;				// a Graphics2D object as canvas for drawing
	private int width=0, height=0;				// image width and height
	private int max_recursion_level = 0;		// maximum recursion level
	private String fractal_type = "Koch Curve";	// type of fractal
	private Color color = Color.green;			// draw color
	
	public void setGraphics(Graphics g, int w, int h)	{
		g2d = (Graphics2D)g; width = w; height = h;
	}
	public void setFractalType(String t)	{ fractal_type = t; }
	public void setColor(Color c)			{ color = c; }
	public void setMaxRecursion(int n)		{ max_recursion_level = n; }

	// Recursive method for drawing the Koch curve given two points and the recursion level
	private void drawKochCurve(Point2D p_1, Point2D p_2, int level) {
		if(level==0) {	// base case
			drawLine(p_1, p_2);
			return;
		}
		Turtle turtle = new Turtle(p_1, p_2);
		double len = p_1.distance(p_2);
		turtle.move(len/3);
		Point2D p_3 = turtle.getPosition();
		turtle.turnLeft(60);
		turtle.move(len/3);
		Point2D p_4 = turtle.getPosition();
		turtle.turnRight(120);
		turtle.move(len/3);
		Point2D p_5 = turtle.getPosition();
		turtle.turnLeft(60);
		turtle.move(len/3);
		drawKochCurve(p_1,p_3, level-1);
		drawKochCurve(p_3,p_4, level-1);
		drawKochCurve(p_4,p_5, level-1);
		drawKochCurve(p_5,p_2, level-1);
		// Koch subdivision rule: ___ ->  _/\_
	}
	
	// Recursive method for drawing a fractal Tree given two points and the recursion level
	private void drawTree(Point2D p_1, Point2D p_2, int level) {
		if(level==0) {
			drawLine(p_1, p_2);
			return;
		}
		Turtle turtle = new Turtle(p_1, p_2);
		double len = p_1.distance(p_2);
		turtle.move(len/3);
		Point2D p_3 = turtle.getPosition();
		turtle.turnLeft(60);
		turtle.move(2*len/3);
		Point2D p_4 = turtle.getPosition();
		turtle.turnRight(180);
		turtle.move(2*len/3);
		turtle.turnLeft(120);
		turtle.turnRight(15);
		turtle.move(2*len/3);
		Point2D p_5 = turtle.getPosition();
		drawLine(p_1,p_3);
		drawTree(p_3,p_4,level-1);
		drawTree(p_3,p_5,level-1);
	}
	
	// Recursive method for drawing the Sierpinski Triangle given the three points
	// that define the triangle and the recursion level
	private void drawSierpinskiTriangle(Point2D p_1, Point2D p_2, Point2D p_3, int level) {
		if(level==0) {	// base case
			drawTriangle(p_1, p_2, p_3);
			return;
		}
		Point2D baseHalf = new Point2D.Double((p_1.getX()+p_2.getX())/2, (p_1.getY()+p_2.getY())/2);
		Point2D leftHalf = new Point2D.Double((p_1.getX()+p_3.getX())/2, (p_1.getY()+p_3.getY())/2);
		Point2D rightHalf = new Point2D.Double((p_2.getX()+p_3.getX())/2, (p_2.getY()+p_3.getY())/2);
	
		drawSierpinskiTriangle(p_1,baseHalf,leftHalf,level-1);
		drawSierpinskiTriangle(baseHalf,p_2,rightHalf,level-1);
		drawSierpinskiTriangle(leftHalf,rightHalf,p_3,level-1);
	}
	
	// Sierpinski Carpet draw, given  lower-left corner of the square (p),  side length (a) of the square, and  recursion level
	private void drawSierpinskiCarpet(Point2D p, double a, int level) {
		if(level==0) {	// base case
			drawRectangle(p, a, a);
			return;
		}
		drawSierpinskiCarpet(p,a/3,level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX()+a/3, p.getY()), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX()+2*a/3, p.getY()), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX()+2*a/3, p.getY()+a/3), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX()+2*a/3, p.getY()+2*a/3), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX()+a/3, p.getY()+2*a/3), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX(), p.getY()+2*a/3), a/3, level-1);
		drawSierpinskiCarpet(new Point2D.Double(p.getX(), p.getY()+a/3), a/3, level-1);
	}
	
	// This method is left for you to experiment with creative fractals
	// designed by yourself. You will NOT be graded on this method 
	void drawMyFractal(/* other parameters that you may need */ int level) {
		if(level==0) {	
			return;
		}
	}
	
	/** The code below provides utility methods.
	 *  You should NOT need to modify any code below.
	 */
	public void draw() {
		if(g2d==null || width==0 || height==0) return;
		g2d.setBackground(Color.black);
		g2d.clearRect(0, 0, width, height);
		g2d.setColor(color);
		if(fractal_type.equalsIgnoreCase("Koch Curve")) {
			drawKochCurve(new Point2D.Double(0.0, 0.4), new Point2D.Double(1.0, 0.4), max_recursion_level);
		} else if(fractal_type.equalsIgnoreCase("Snowflake")) {
			double r = 0.5;
			Point2D p1 = new Point2D.Double(r*Math.cos(Math.toRadians(150))+0.5,
											r*Math.sin(Math.toRadians(150))+0.5);
			Point2D p2 = new Point2D.Double(r*Math.cos(Math.toRadians(30))+0.5,
											r*Math.sin(Math.toRadians(30))+0.5);
			Point2D p3 = new Point2D.Double(r*Math.cos(Math.toRadians(-90))+0.5,
											r*Math.sin(Math.toRadians(-90))+0.5);
			//  p1____p2
			//    \  /
			//     \/
			//     p3
			drawKochCurve(p1, p2, max_recursion_level);
			drawKochCurve(p2, p3, max_recursion_level);
			drawKochCurve(p3, p1, max_recursion_level);
		} else if(fractal_type.equalsIgnoreCase("Tree")) {
			drawTree(new Point2D.Double(0.6, 0.1), new Point2D.Double(0.6, 0.9),
					max_recursion_level*2);
		} else if(fractal_type.equalsIgnoreCase("Sp Triangle")) {
			double r = 0.5;
			Point2D p1 = new Point2D.Double(r*Math.cos(Math.toRadians(90))+0.5,
											r*Math.sin(Math.toRadians(90))+0.5);
			Point2D p2 = new Point2D.Double(r*Math.cos(Math.toRadians(-150))+0.5,
											r*Math.sin(Math.toRadians(-150))+0.5);
			Point2D p3 = new Point2D.Double(r*Math.cos(Math.toRadians(-30))+0.5,
											r*Math.sin(Math.toRadians(-30))+0.5);
			drawSierpinskiTriangle(p1, p2, p3, max_recursion_level);
		} else if(fractal_type.equalsIgnoreCase("Sp Carpet")) {
			drawSierpinskiCarpet(new Point2D.Double(0, 0), 1, max_recursion_level);
		} else {
			drawMyFractal(max_recursion_level);
		}
	}
	/** Draw a straight line between two points P1 and P2.
	 * The given x and y values of p1 and p2 are assumed to be within [0, 1] (i.e. normalized).
	 * This allows our fractals to be resolution-independent. The method below converts the normalized
	 * coordinates to integer coordinates based on the actual image resolution. 
	 */
	private void drawLine(Point2D p1, Point2D p2) {
		int x1 = (int)(p1.getX()*width);
		int x2 = (int)(p2.getX()*width);
		int y1 = (int)((1.0-p1.getY())*height);
		int y2 = (int)((1.0-p2.getY())*height);
		g2d.drawLine(x1, y1, x2, y2);
	}
	
	private void drawRectangle(Point2D p, double w, double h) {
		int x0 = (int)(p.getX()*width);
		int y0 = (int)((1.0-p.getY())*height);
		int x1 = (int)((p.getX()+w)*width);;
		int y1 = (int)((1.0-(p.getY()+h))*height);
		int xpoints[] = {x0, x0, x1, x1};
		int ypoints[] = {y0, y1, y1, y0};
		g2d.fillPolygon(xpoints, ypoints, 4);
	}
	
	private void drawTriangle(Point2D p1, Point2D p2, Point2D p3) {
		int xpoints[] = {(int)(p1.getX()*width),
						 (int)(p2.getX()*width),
						 (int)(p3.getX()*width)};
		int ypoints[] = {(int)((1.0-p1.getY())*height),
						 (int)((1.0-p2.getY())*height),
						 (int)((1.0-p3.getY())*height)};
		g2d.fillPolygon(xpoints, ypoints, 3);
	}
}


