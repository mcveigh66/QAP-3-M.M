// Desc:
// Author:
// Dates:


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

// Define program constants.
const BORDER_PRICE = 0.04;
const BORDER_PER = 0.28;
const LAWN_MOVING = 0.95;
const LAWN_MOVING_PER = 0.04;
const FERT_TREATMENT = 0.03;
const HST_RATE = 0.15;
const ENVIRO_TAX = 1.4;

// Start main program here.
let CustName = prompt("Enter the customer name:   ")
let StreetAdd = prompt("Enter the customer street address:   ")
let PhoneNum = prompt("Enter the customer phone number:   ")
let City = prompt("Enter the customers City:   ")
let TotSqFt = prompt("Enter the total square footage of the lawn:\n");

// Calculations 
let BorderSize = TotSqFt * BORDER_PRICE;
let BorderCost = BorderSize * BORDER_PER;
let LawnMove = TotSqFt * LAWN_MOVING;
let LawnMovePrice = LawnMove * LAWN_MOVING_PER;
let FertTreat = TotSqFt * FERT_TREATMENT;
let TotCharges = BorderCost + LawnMovePrice + FertTreat; 
let SalesTax = TotCharges * HST_RATE;
let EnviroTax = TotCharges * ENVIRO_TAX;
let InvTot = TotCharges + SalesTax + EnviroTax;


// Display output 
document.writeln("<br /><table class='lawntable'>");

// Title row
document.writeln("<tr>");
document.writeln("<th colspan='2' class='orangeback'>Mo's Lawncare Services - Customer Invoice</th>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2'>");

document.writeln("<br />");
document.writeln("&nbsp;&nbsp;Customer details:<br />");
document.writeln("<br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp" + (CustName) + "<br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp" + (StreetAdd) + "<br />");
document.writeln("&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp" + (City) + "&nbsp;" + (PhoneNum) + "<br />");
document.writeln("</div>");
document.writeln("<br />");
document.writeln("&nbsp;&nbsp;Property size (in sq ft):" + (TotSqFt) + "<br />");
document.writeln("<br />");

document.writeln("</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Border Cost:</td>");
document.writeln("<td class='righttext'>" + cur2Format.format(BorderCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Mowing Cost:</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(LawnMovePrice) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Fertilizer Cost:</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(FertTreat) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td></td>")
document.writeln("<td class='righttext'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Total charges:</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(TotCharges) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td></td>")
document.writeln("<td class='righttext'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Sales tax(HST):</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(SalesTax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Environmental tax:</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(EnviroTax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td></td>")
document.writeln("<td class='righttext'>&nbsp;</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td>Invoice total:</td>");
document.writeln("<td class ='righttext'>" + cur2Format.format(InvTot) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan='2' class='orangebacktwo'>Turning Lawns into Landscapes</td>");
document.writeln("</tr>");

document.writeln("</table>");


