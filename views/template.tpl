<!doctype html>
<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
   <meta charset="utf-8">

   <!-- Use the .htaccess and remove these lines to avoid edge case issues.
   More info: h5bp.com/i/378 -->
   <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">

   <title>k-means experimentation</title>
   <meta name="description" content="">

   <!-- Mobile viewport optimized: h5bp.com/viewport -->
   <meta name="viewport" content="width=device-width">

   <!-- Place favicon.ico and apple-touch-icon.png in the
   root directory: mathiasbynens.be/notes/touch-icons -->

   <link rel="stylesheet" href="{{ get_url('static', path='style.css') }}">
   <script type="text/javascript" src="{{ get_url('static', path='jquery-1.7.2.js') }}"></script>
   <script type="text/javascript" src="{{ get_url('static', path='raphael.js') }}"></script>
   <script type="text/javascript" src="{{ get_url('static', path='g.raphael-min.js') }}"></script>
   <script type="text/javascript" src="{{ get_url('static', path='json2.js') }}"></script>
</head>
<body>
   <!-- Prompt IE 6 users to install Chrome Frame. Remove this if you support IE 6.  chromium.org/developers/how-tos/chrome-frame-getting-started -->
   <!--[if lt IE 7]><p class=chromeframe>Your browser is <em>ancient!</em> <a href="http://browsehappy.com/">Upgrade to a different browser</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to experience this site.</p><![endif]-->

%for key, cluster in clusters.items():
   <span id="{{ key }}" data-points="
%for point in cluster:
{{ map(int, list(point)) }}
%end 
"></span>
%end

   <!-- JavaScript at the bottom for fast page loading: http://developer.yahoo.com/performance/rules.html#js_bottom -->
   <script type="text/javascript">
      // Creates canvas 320 × 200 at 10, 50
      var paper = Raphael(10, 50, 400, 800);

      var k = {{ k }}

      data = []
      for (i = 0; i < k; i++) {
         data[i] = JSON.parse(JSON.stringify($('#'+i).data('points')));
      }

      console.log(data);

      // Creates circle at x = 50, y = 40, with radius 10
      var circle = paper.circle(50, 40, 1);
      // Sets the fill attribute of the circle to red (#f00)
      circle.attr("fill", "#f00");

      // Sets the stroke attribute of the circle to white
      circle.attr("stroke", "#fff");
   </script>


</body>
</html>
