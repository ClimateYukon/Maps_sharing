import dash_trich_components as dtc
import dash_html_components as html

carousel = dtc.Carousel([
           	html.Div('slide 1'),
 			html.Div('slide 2'),
  			html.Div('slide 3'),
  			html.Div('slide 4'),
  			html.Div('slide 5'),
  			html.Div('slide 6')
		],
            slides_to_scroll=1,
            swipe_to_slide=True,
            autoplay=True,
            speed=2000,
            variable_width=True,
            center_mode=True,
            responsive=[
            {
                'breakpoint': 991,
                'settings': {
                    'arrows': False
                }
            }]
		)
