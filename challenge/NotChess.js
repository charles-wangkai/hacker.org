// Q: http://www.hacker.org/challenge/chal.php?id=68
// A: http://www.hacker.org/challenge/chal.php?answer=queen%27s+gambit&id=68&go=Submit

var keyStr = "ABCDEFGHIJKLMNOP" + "QRSTUVWXYZabcdef" + "ghijklmnopqrstuv"
		+ "wxyz0123456789+/" + "=";

function encodeIt(input, toEscape) {
	toEscape = typeof toEscape !== 'undefined' ? toEscape : true;
	
	if (toEscape) {
		input = escape(input);
	}
	var output = "";
	var chr1, chr2, chr3 = "";
	var enc1, enc2, enc3, enc4 = "";
	var i = 0;

	do {
		chr1 = input.charCodeAt(i++);
		chr2 = input.charCodeAt(i++);
		chr3 = input.charCodeAt(i++);

		enc1 = chr1 >> 2;
		enc2 = ((chr1 & 3) << 4) | (chr2 >> 4);
		enc3 = ((chr2 & 15) << 2) | (chr3 >> 6);
		enc4 = chr3 & 63;

		if (isNaN(chr2)) {
			enc3 = enc4 = 64;
		} else if (isNaN(chr3)) {
			enc4 = 64;
		}

		output = output + keyStr.charAt(enc1) + keyStr.charAt(enc2)
				+ keyStr.charAt(enc3) + keyStr.charAt(enc4);
		chr1 = chr2 = chr3 = "";
		enc1 = enc2 = enc3 = enc4 = "";
	} while (i < input.length);

	return output;
}

function ff(answer) {
	v = encodeIt(answer);
	if (v == 'cXVlZW4lMjdzJTIwZ2FtYml0') {
		return true;
	} else {
		alert("not it! you typed: " + v);
		return false;
	}
}

var search = function(code) {
	for (var chr1 = 0; chr1 < 128; chr1++) {
		for (var chr2 = 0; chr2 < 128; chr2++) {
			for (var chr3 = 0; chr3 < 128; chr3++) {
				var original = String.fromCharCode(chr1, chr2, chr3);
				if (encodeIt(original, false) === code) {
					return original;
				}
			}
		}
	}
}

var target = 'cXVlZW4lMjdzJTIwZ2FtYml0';
var original = '';
for (var i = 0; i < target.length; i += 4) {
	original += search(target.substr(i, 4));
}
console.log(unescape(original));
