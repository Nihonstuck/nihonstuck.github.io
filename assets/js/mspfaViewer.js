  } else if (p == 8127) {
    document.getElementById("cssSet").href = "/assets/css/act7style.css";
    document.getElementById("headerDiv").style.display = "flex";
    document.getElementById("headerImg").src = "/assets/images/act7_header.gif";
  } else if (5714 <= p && p <= 5777) {
    document.getElementById("cssSet").href = "/assets/css/trickster.css";
    document.getElementById("headerDiv").style.display = "flex";
    document.getElementById("headerImg").outerHTML =
      '<object id="headerImg" type="application/x-shockwave-flash" ' +
      'data="/assets/images/trickster_sitegraphics/menu.swf" ' +
      'width="950" height="20"></object>';
  } else if (
    (6242 < p && p < 6277) ||
    (6474 < p && p < 6530) ||
    (6852 < p && p < 6900) ||
    (6921 < p && p < 6943) ||
    (7408 < p && p < 7448)
  ) {
    document.getElementById("cssSet").href = "/assets/css/homosuck.css";
    document.getElementById("headerDiv").style.display = "none";
    document.getElementById("headerImg").src = "";
   
  } else if (
    (p == 5495) ||
    (p == 5780) ||
    (p == 6278) ||
    (6315 < p && p < 6318) ||
    (6355 < p && p < 6359) ||
    (p == 6382) ||
    (6383 < p && p < 6387) ||
    (6387 < p && p < 6392) ||
    (p == 6397) ||
    (6400 < p && p < 6404) ||
    (p == 6405) ||
    (6408 < p && p < 6411) ||
    (6414 < p && p < 6420) ||
    (6437 < p && p < 6440) ||
    (p == 6901) ||
    (p == 7959) ||
    (8088 < p && p < 8127) 
      
  ) {
    document.getElementById("cssSet").href = "/assets/css/bigstyle.css";
    document.getElementById("headerDiv").style.display = "none";
    document.getElementById("headerImg").src = "";
  } else {
    document.getElementById("cssSet").href = "/assets/css/uhcstyle.css";
    document.getElementById("headerDiv").style.display = "none";
    document.getElementById("headerImg").src = "";
  }
  };