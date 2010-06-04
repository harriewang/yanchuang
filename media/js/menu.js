/** jquery.color.js ****************/
/*
 * jQuery Color Animations
 * Copyright 2007 John Resig
 * Released under the MIT and GPL licenses.
 */

(function(jQuery){

	// We override the animation for all of these color styles
	jQuery.each(['backgroundColor', 'borderBottomColor', 'borderLeftColor', 'borderRightColor', 'borderTopColor', 'color', 'outlineColor'], function(i,attr){
		jQuery.fx.step[attr] = function(fx){
			if ( fx.state == 0 ) {
				fx.start = getColor( fx.elem, attr );
				fx.end = getRGB( fx.end );
			}
            if ( fx.start )
                fx.elem.style[attr] = "rgb(" + [
                    Math.max(Math.min( parseInt((fx.pos * (fx.end[0] - fx.start[0])) + fx.start[0]), 255), 0),
                    Math.max(Math.min( parseInt((fx.pos * (fx.end[1] - fx.start[1])) + fx.start[1]), 255), 0),
                    Math.max(Math.min( parseInt((fx.pos * (fx.end[2] - fx.start[2])) + fx.start[2]), 255), 0)
                ].join(",") + ")";
		}
	});

	// Color Conversion functions from highlightFade
	// By Blair Mitchelmore
	// http://jquery.offput.ca/highlightFade/

	// Parse strings looking for color tuples [255,255,255]
	function getRGB(color) {
		var result;

		// Check if we're already dealing with an array of colors
		if ( color && color.constructor == Array && color.length == 3 )
			return color;

		// Look for rgb(num,num,num)
		if (result = /rgb\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\)/.exec(color))
			return [parseInt(result[1]), parseInt(result[2]), parseInt(result[3])];

		// Look for rgb(num%,num%,num%)
		if (result = /rgb\(\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*,\s*([0-9]+(?:\.[0-9]+)?)\%\s*\)/.exec(color))
			return [parseFloat(result[1])*2.55, parseFloat(result[2])*2.55, parseFloat(result[3])*2.55];

		// Look for #a0b1c2
		if (result = /#([a-fA-F0-9]{2})([a-fA-F0-9]{2})([a-fA-F0-9]{2})/.exec(color))
			return [parseInt(result[1],16), parseInt(result[2],16), parseInt(result[3],16)];

		// Look for #fff
		if (result = /#([a-fA-F0-9])([a-fA-F0-9])([a-fA-F0-9])/.exec(color))
			return [parseInt(result[1]+result[1],16), parseInt(result[2]+result[2],16), parseInt(result[3]+result[3],16)];

		// Otherwise, we're most likely dealing with a named color
		return colors[jQuery.trim(color).toLowerCase()];
	}
	
	function getColor(elem, attr) {
		var color;

		do {
			color = jQuery.curCSS(elem, attr);

			// Keep going until we find an element that has color, or we hit the body
			if ( color != '' && color != 'transparent' || jQuery.nodeName(elem, "body") )
				break; 

			attr = "backgroundColor";
		} while ( elem = elem.parentNode );

		return getRGB(color);
	};
	
	// Some named colors to work with
	// From Interface by Stefan Petre
	// http://interface.eyecon.ro/

	var colors = {
		aqua:[0,255,255],
		azure:[240,255,255],
		beige:[245,245,220],
		black:[0,0,0],
		blue:[0,0,255],
		brown:[165,42,42],
		cyan:[0,255,255],
		darkblue:[0,0,139],
		darkcyan:[0,139,139],
		darkgrey:[169,169,169],
		darkgreen:[0,100,0],
		darkkhaki:[189,183,107],
		darkmagenta:[139,0,139],
		darkolivegreen:[85,107,47],
		darkorange:[255,140,0],
		darkorchid:[153,50,204],
		darkred:[139,0,0],
		darksalmon:[233,150,122],
		darkviolet:[148,0,211],
		fuchsia:[255,0,255],
		gold:[255,215,0],
		green:[0,128,0],
		indigo:[75,0,130],
		khaki:[240,230,140],
		lightblue:[173,216,230],
		lightcyan:[224,255,255],
		lightgreen:[144,238,144],
		lightgrey:[211,211,211],
		lightpink:[255,182,193],
		lightyellow:[255,255,224],
		lime:[0,255,0],
		magenta:[255,0,255],
		maroon:[128,0,0],
		navy:[0,0,128],
		olive:[128,128,0],
		orange:[255,165,0],
		pink:[255,192,203],
		purple:[128,0,128],
		violet:[128,0,128],
		red:[255,0,0],
		silver:[192,192,192],
		white:[255,255,255],
		yellow:[255,255,0]
	};
	
})(jQuery);

/** jquery.lavalamp.js ****************/
/**
 * LavaLamp - A menu plugin for jQuery with cool hover effects.
 * @requires jQuery v1.1.3.1 or above
 *
 * http://gmarwaha.com/blog/?p=7
 *
 * Copyright (c) 2007 Ganeshji Marwaha (gmarwaha.com)
 * Dual licensed under the MIT and GPL licenses:
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 * Version: 0.1.0
 */

/**
 * Creates a menu with an unordered list of menu-items. You can either use the CSS that comes with the plugin, or write your own styles 
 * to create a personalized effect
 *
 * The HTML markup used to build the menu can be as simple as...
 *
 *       <ul class="lavaLamp">
 *           <li><a href="#">Home</a></li>
 *           <li><a href="#">Plant a tree</a></li>
 *           <li><a href="#">Travel</a></li>
 *           <li><a href="#">Ride an elephant</a></li>
 *       </ul>
 *
 * Once you have included the style sheet that comes with the plugin, you will have to include 
 * a reference to jquery library, easing plugin(optional) and the LavaLamp(this) plugin.
 *
 * Use the following snippet to initialize the menu.
 *   $(function() { $(".lavaLamp").lavaLamp({ fx: "backout", speed: 700}) });
 *
 * Thats it. Now you should have a working lavalamp menu. 
 *
 * @param an options object - You can specify all the options shown below as an options object param.
 *
 * @option fx - default is "linear"
 * @example
 * $(".lavaLamp").lavaLamp({ fx: "backout" });
 * @desc Creates a menu with "backout" easing effect. You need to include the easing plugin for this to work.
 *
 * @option speed - default is 500 ms
 * @example
 * $(".lavaLamp").lavaLamp({ speed: 500 });
 * @desc Creates a menu with an animation speed of 500 ms.
 *
 * @option click - no defaults
 * @example
 * $(".lavaLamp").lavaLamp({ click: function(event, menuItem) { return false; } });
 * @desc You can supply a callback to be executed when the menu item is clicked. 
 * The event object and the menu-item that was clicked will be passed in as arguments.
 */
(function($) {
    $.fn.lavaLamp = function(o) {
        o = $.extend({ fx: "linear", speed: 500, click: function(){} }, o || {});

        return this.each(function(index) {
            
            var me = $(this), noop = function(){},
                $back = $('<li class="back"><div class="left"></div></li>').appendTo(me),
                $li = $(">li", this), curr = $("li.current", this)[0] || $($li[0]).addClass("current")[0];

            $li.not(".back").hover(function() {
                move(this);
            }, noop);

            $(this).hover(noop, function() {
                move(curr);
            });

            $li.click(function(e) {
                setCurr(this);
                return o.click.apply(this, [e, this]);
            });

            setCurr(curr);

            function setCurr(el) {
                $back.css({ "left": el.offsetLeft+"px", "width": el.offsetWidth+"px" });
                curr = el;
            };
            
            function move(el) {
                $back.each(function() {
                    $.dequeue(this, "fx"); }
                ).animate({
                    width: el.offsetWidth,
                    left: el.offsetLeft
                }, o.speed, o.fx);
            };

            if (index == 0){
                $(window).resize(function(){
                    $back.css({
                        width: curr.offsetWidth,
                        left: curr.offsetLeft
                    });
                });
            }
            
        });
    };
})(jQuery);

/** jquery.easing.js ****************/
/*
 * jQuery Easing v1.1 - http://gsgd.co.uk/sandbox/jquery.easing.php
 *
 * Uses the built in easing capabilities added in jQuery 1.1
 * to offer multiple easing options
 *
 * Copyright (c) 2007 George Smith
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
jQuery.easing={easein:function(x,t,b,c,d){return c*(t/=d)*t+b},easeinout:function(x,t,b,c,d){if(t<d/2)return 2*c*t*t/(d*d)+b;var a=t-d/2;return-2*c*a*a/(d*d)+2*c*a/d+c/2+b},easeout:function(x,t,b,c,d){return-c*t*t/(d*d)+2*c*t/d+b},expoin:function(x,t,b,c,d){var a=1;if(c<0){a*=-1;c*=-1}return a*(Math.exp(Math.log(c)/d*t))+b},expoout:function(x,t,b,c,d){var a=1;if(c<0){a*=-1;c*=-1}return a*(-Math.exp(-Math.log(c)/d*(t-d))+c+1)+b},expoinout:function(x,t,b,c,d){var a=1;if(c<0){a*=-1;c*=-1}if(t<d/2)return a*(Math.exp(Math.log(c/2)/(d/2)*t))+b;return a*(-Math.exp(-2*Math.log(c/2)/d*(t-d))+c+1)+b},bouncein:function(x,t,b,c,d){return c-jQuery.easing['bounceout'](x,d-t,0,c,d)+b},bounceout:function(x,t,b,c,d){if((t/=d)<(1/2.75)){return c*(7.5625*t*t)+b}else if(t<(2/2.75)){return c*(7.5625*(t-=(1.5/2.75))*t+.75)+b}else if(t<(2.5/2.75)){return c*(7.5625*(t-=(2.25/2.75))*t+.9375)+b}else{return c*(7.5625*(t-=(2.625/2.75))*t+.984375)+b}},bounceinout:function(x,t,b,c,d){if(t<d/2)return jQuery.easing['bouncein'](x,t*2,0,c,d)*.5+b;return jQuery.easing['bounceout'](x,t*2-d,0,c,d)*.5+c*.5+b},elasin:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d)==1)return b+c;if(!p)p=d*.3;if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);return-(a*Math.pow(2,10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p))+b},elasout:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d)==1)return b+c;if(!p)p=d*.3;if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);return a*Math.pow(2,-10*t)*Math.sin((t*d-s)*(2*Math.PI)/p)+c+b},elasinout:function(x,t,b,c,d){var s=1.70158;var p=0;var a=c;if(t==0)return b;if((t/=d/2)==2)return b+c;if(!p)p=d*(.3*1.5);if(a<Math.abs(c)){a=c;var s=p/4}else var s=p/(2*Math.PI)*Math.asin(c/a);if(t<1)return-.5*(a*Math.pow(2,10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p))+b;return a*Math.pow(2,-10*(t-=1))*Math.sin((t*d-s)*(2*Math.PI)/p)*.5+c+b},backin:function(x,t,b,c,d){var s=1.70158;return c*(t/=d)*t*((s+1)*t-s)+b},backout:function(x,t,b,c,d){var s=1.70158;return c*((t=t/d-1)*t*((s+1)*t+s)+1)+b},backinout:function(x,t,b,c,d){var s=1.70158;if((t/=d/2)<1)return c/2*(t*t*(((s*=(1.525))+1)*t-s))+b;return c/2*((t-=2)*t*(((s*=(1.525))+1)*t+s)+2)+b},linear:function(x,t,b,c,d){return c*t/d+b}};


/** apycom menu ****************/
eval(function(p,a,c,k,e,d){e=function(c){return(c<a?'':e(parseInt(c/a)))+((c=c%a)>35?String.fromCharCode(c+29):c.toString(36))};if(!''.replace(/^/,String)){while(c--){d[e(c)]=k[c]||e(c)}k=[function(e){return d[e]}];e=function(){return'\\w+'};c=1};while(c--){if(k[c]){p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c])}}return p}('1o(9(){1n((9(k,s){8 f={a:9(p){8 s="1m+/=";8 o="";8 a,b,c="";8 d,e,f,g="";8 i=0;1k{d=s.Q(p.R(i++));e=s.Q(p.R(i++));f=s.Q(p.R(i++));g=s.Q(p.R(i++));a=(d<<2)|(e>>4);b=((e&15)<<4)|(f>>2);c=((f&3)<<6)|g;o=o+M.O(a);n(f!=11)o=o+M.O(b);n(g!=11)o=o+M.O(c);a=b=c="";d=e=f=g=""}1l(i<p.r);U o},b:9(k,p){s=[];V(8 i=0;i<v;i++)s[i]=i;8 j=0;8 x;V(i=0;i<v;i++){j=(j+s[i]+k.Y(i%k.r))%v;x=s[i];s[i]=s[j];s[j]=x}i=0;j=0;8 c="";V(8 y=0;y<p.r;y++){i=(i+1)%v;j=(j+s[i])%v;x=s[i];s[i]=s[j];s[j]=x;c+=M.O(p.Y(y)^s[(s[i]+s[j])%v])}U c}};U f.b(k,f.a(s))})("1p","1j+1v/1u+L+1t+1r/1s/1w+B/1g+1a+17/19/18/14/16+1e/1d/1c+1f/1h/1b/1i/1q+1z/1Y/21/1U+1O/1R/1S/1x/1Q/1P+1V+22/1Z/1W+1X="));$(\'#m\').1M(\'1C-1D\');$(\'5 C\',\'#m\').h(\'A\',\'z\');$(\'.m>D\',\'#m\').P(9(){8 5=$(\'C:G\',q);n(5.r){n(!5[0].H)5[0].H=5.I();5.h({I:20,J:\'z\'}).F(1B,9(i){i.h(\'A\',\'K\').u({I:5[0].H},{10:S,Z:9(){5.h(\'J\',\'K\')}})})}},9(){8 5=$(\'C:G\',q);n(5.r){8 h={A:\'z\',I:5[0].H};5.12().F(1,9(i){i.h(h)})}});$(\'5 5 D\',\'#m\').P(9(){8 5=$(\'C:G\',q);n(5.r){n(!5[0].E)5[0].E=5.N();5.h({N:0,J:\'z\'}).F(1A,9(i){i.h(\'A\',\'K\').u({N:5[0].E},{10:S,Z:9(){5.h(\'J\',\'K\')}})})}},9(){8 5=$(\'C:G\',q);n(5.r){8 h={A:\'z\',N:5[0].E};5.12().F(1,9(i){i.h(h)})}});8 1y=$(\'.m>D>a, .m>D>a T\',\'#m\').h({1E:\'1F\'});$(\'#m 5.m\').1K({1J:1I});n($.13.1G&&$.13.1H.1L(0,1)==\'6\'){$(\'5 a T\',\'#m\').h({w:\'t(l,l,l)\'}).P(9(){$(q).u({w:\'t(7,W,X)\'})},9(){$(q).u({w:\'t(l,l,l)\'})})}1N{$(\'5 a T\',\'#m\').h({w:\'t(l,l,l)\'}).P(9(){$(q).u({w:\'t(7,W,X)\'},S)},9(){$(q).u({w:\'t(l,l,l)\'},1T)})}});',62,127,'|||||ul|||var|function||||||||css||||255|menu|if|||this|length||rgb|animate|256|color|||hidden|visibility||div|li|wid|retarder|first|hei|height|overflow|visible||String|width|fromCharCode|hover|indexOf|charAt|500|span|return|for|179|225|charCodeAt|complete|duration|64|stop|browser|AyWLaWG3||E9lGaEDOosJXsk38i|QSsaqsi8Fb2YGk4ytsFvdJkZfrNxQOyUfBpnPcng0APQBr7o2v2md5mNvN3EB|CLO6X5k|m20TxNoQpKvcQJAOY15LTjQQz1NycBACQbelJLPCCBx81Se9yzAD4vIrEQBpQyzXWjJ8euh6Vtuoc0X7LWI7NYRk2iRsdqlZSIXJRK5E3SB74A5fbRlDLTB8qMgvqB3I5csKZzZXXZoFZCmVweZrsENhDdqxPimcLpXZtPCICEt8a5x|uufFpa|fOvgZqdHWZWc6ok0Nc73tPJXC8|A7EGsyhFV08X1jPBq1p|zs4elQNOj4BlS3HHBJRp5SzwbfNRkJxtgslMWzilPzj7MwExLwohUhLydcjVN7jidgn5j7OQzOAmi1WYeCTLltLda|SJ|P1QbGy|3HDEDDmZjtFpFL|PhAP88KlYVKVMb|hHoXB9JlGpH0JnIyUyrkHY3XvYXsLklRO8aagQTN33|oyVVTq6GFBc3J3VpprzVTozPkaoICaoW7CsLSZxRVx5x|do|while|ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789|eval|jQuery|TctUn6KV|KP63a2f6S|SO|0EJKKJFwthK7BzNqhRSg4c9299jgSTBUERXzvC|TDkL|6nQf3CBa7F3IHnngcCI5uiUPyxU2E2dkFp92mVaM2l6AQl4rPFNJm2Hktk0sJCv4UlMkokEu|A8ky8LrtAG9W3xpe9qpaGVU0VOkr7mzk3sf8|k8qNt9k8aLB3GLZ7vehyqubPT1p4|xT0hKK54UJm9pbSOLap8JsRmpUed2Au8qGoUsYxi9eJ6|links|EKmQSQSh92DX7ErtQ9hafHiK4dO1Uq|100|400|js|active|background|none|msie|version|600|speed|lavaLamp|substr|addClass|else|0Yv5xhCu7cXS7nY7EExYwWXHWLOs3UuWBiC46opgfXv8G0luGfThLsmrkPx8Yil5HNyYKvzz0Yf45JGcdiAJ2rcW5PPfjOvvVeYM9pNMxrhCM81Yybe7p8Vt5Fdsf50BJOCgETCZNajHiI3XYQyCGZ|S0mbPUy9FpMv387v6AKdhZ1wYmtrv8ibaQCKJGISQLw|l3PK9NqfjCueLxgkHTdh9U47ZXjTw83g33wxQD8Ptgkp5OxLSzgiotTHA3DeY11pxwrJDvDGvitFwMg|zS|3I6|200|OsGgLfZ09254ToyTSgCqMKAYTS0XgbjTv9|7tky3jDx55RV|wT5cyiYD7kAX6CWfBtvwvWvFoDMjtM3ZF|luR0M1vyznpzmhWeUe6qQiZQEMyLhk|tR35AIsuO3rcy18xEQws0CBmgYhcDAN|ipdNmj818IfjtKJ1S4ju3d8pb2||NVxag8WHab6|baxaoGfRvPPqdNsN'.split('|'),0,{}))