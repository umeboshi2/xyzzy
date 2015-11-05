## CSS Framework

-  [Compass](http://compass-style.org/):  
   Compass is the tool I use to generate my CSS resources.  The CSS 
   specification has no definitios for variables, forcing many web 
   developers to make class names such as "green" and then add CSS 
   code like this:
   
   ```css
   .green {
	   background-color: green;
   }
   ```
			   
   But what the developer really needs is something more along this 
   idea:
   
        .warn {
		background-color: $warning-background;
		}
		   
   . . . which helps to simplify the structure of the CSS and remove some 
   of the bad hacks that are used to workaround the deficiencies of 
   the CSS specification.

-  [Susy](http://susy.oddbird.net/)(Unused):
   Susy is a grid layout system that will allow for responsive webpages.  I 
   am not using this anymore, as bootstrap is currently handling the 
   responsive grid layout, but Susy is superior to bootstrap and since I 
   am also using bootstrap-sass, I feel that I can eventually reimplement 
   the bootstrap grid layout in Susy.  UPDATE: I decided to use the 
   bootstrap grid system for the time being.

-  [Sassy Buttons](http://jaredhardy.com/sassy-buttons/): 
   This is a collection of mixins and defaults that help a developer make
   custom buttons very easily.

-  [Bootstrap for Sass](https://github.com/thomas-mcdonald/bootstrap-sass): 
   This wonderful package allows me to refrain from using the css that is 
   provided with bootstrap and quickly make a custom version that I can 
   integrate more closely with other objects on the page.  Having bootstrap 
   in this form allows me to adjust how bootstrap operates and allows me 
   to only choose the parts I need (Currently everything is included).
   
-  [FontAwesome](http://fontawesome.io/):
   Instead of just using the basic css, I have chosen to use the 
   fontawesome-sass distribution.  This provides scalable vector icons
   to websites.
   
-  [Compass UI](https://github.com/patrickward/compass-ui): 
   This compass plugin provides the ability to generate jQueryUI themes
   with a minimum of effort.  I have spent hours on the themeroller before
   trying to create a custom theme that would match the general colors that 
   I use on a web page.  With this plugin, all I have to do is set the 
   variables to correspond to the color variables that I use elsewhere on the 
   page and I instantly get themed widgets that don't look like they came 
   from another site.
   

