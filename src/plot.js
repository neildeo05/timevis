//https://vega.github.io/vega/docs/expressions/
//https://github.com/vega/vega/issues/17

vega.expressionFunction('DEBUG', function(coords, msg) { 
  console.log(coords)
  console.log(msg)
  return coords;
});

vega.expressionFunction("Test", () => {
  console.log({
		"$schema": "https://vega.github.io/schema/vega-lite/v5.json",
		"description": "Google's stock price over time.",
		"data": {"url": "data/stocks.csv"},
		"transform": [{"filter": "datum.symbol==='GOOG'"}],
		"mark": "line",
		"encoding": {
			"x": {"field": "date", "type": "temporal"},
			"y": {"field": "price", "type": "quantitative"}
		}
	})
})

vega.expressionFunction("TRYING", (link) => { 
  return link;
})

var obj = {
  "$schema": "https://vega.github.io/schema/vega/v5.json",
  "width": 500,
  "height": 500,
  "padding": 100,
  "autosize": "pad",

  "signals": [
    {
      "name": "margin",
      "value": 20
    },
    {
      "name": "down", "value": null,
      "on": [
        {"events": "mousedown", "update": "xy()"}
      ]
    },
    {
      "name": "xcur", "value": null,
      "on": [
        {
          "events": "mousedown",
          "update": "slice(xdom)"
        }
      ]
    },
    {
      "name": "ycur", "value": null,
      "on": [
        {
          "events": "mousedown",
          "update": "slice(ydom)"
        }
      ]
    },
    {
      "name": "zoomto", "value": null,
      "on": [
        {
          "events": "window:mouseup",
          "update": "(box) || zoomto"
        }
      ]
    },
    {
      "name": "box", "value": null,
      "on": [
        {
          "events": [
            {
              "source": "window",
              "type": "mousemove", "filter": "event.shiftKey",
              "consume": true,
              "between": [
                {"type": "mousedown", "filter": "event.shiftKey"},
                {"source": "window", "type": "mouseup"}]
            }
          ],
          "update": "down ? [x(), y()] : null"
        },
        {
          "events": "window:mouseup",
          "update": "null"
        }
      ]
    },
    {
      "name": "delta", "value": [0, 0],
      "on": [
        {
          "events": [
            {
              "source": "window",
              "type": "mousemove", "filter": "!event.shiftKey",
              "consume": true,
              "between": [
                {"type": "mousedown", "filter": "!event.shiftKey"},
                {"source": "window", "type": "mouseup"}
              ]
            }
          ],
          "update": "down ? [down[0]-x(), y()-down[1]] : [0,0]"
        }
      ]
    },

    {
      "name": "anchor", "value": [0, 0],
      "on": [
        {
          "events": "wheel",
          "update": "[invert('xscale', x()), invert('yscale', y())]"
        }
      ]
    },
    {
      "name": "zoom", "value": 1,
      "on": [
        {
          "events": "wheel!",
          "force": true,
          "update": "pow(1.001, event.deltaY * pow(16, event.deltaMode))"
        }
      ]
    },
    {
      "name": "xdom", "update": "slice(xext)",
      "on": [
        {
          "events": "dblclick",
          "update": "(slice(xext))"
        },
        {
          "events": {"signal": "delta"},
          "update": "[xcur[0] + span(xcur) * delta[0] / width, xcur[1] + span(xcur) * delta[0] / width]"
        },
        {
          "events": {"signal": "zoom"},
          "update": "[anchor[0] + (xdom[0] - anchor[0]) * zoom, anchor[0] + (xdom[1] - anchor[0]) * zoom]"
        },
        {
          "events": {"signal": "zoomto"},
          //THIS IS WHERE THE XBOX CALLS ZOOMTO
          //"update": "DEBUG([invert('xscale', min(down[0], zoomto[0])), invert('xscale', max(down[0], zoomto[0]))],'xzoomto')"
          "update": "Test()"
        }
      ]
    },
    {
      "name": "ydom", "update": "slice(yext)",
      "on": [
        {
          "events": "dblclick",
          "update": "slice(yext)"
        },
        {
          "events": {"signal": "delta"},
          "update": "[ycur[0] + span(ycur) * delta[1] / height, ycur[1] + span(ycur) * delta[1] / height]"
        },
        {
          "events": {"signal": "zoom"},
          "update": "[anchor[1] + (ydom[0] - anchor[1]) * zoom, anchor[1] + (ydom[1] - anchor[1]) * zoom]"
        },
        {
          "events": {"signal": "zoomto"},
          //THIS IS WHERE THE YBOX CALLS ZOOMTO
          "update": "DEBUG([invert('yscale', max(down[1], zoomto[1])), invert('yscale', min(down[1], zoomto[1]))], 'yzoomto')"
        }
      ]
    },
    {
      "name": "size",
      "update": "clamp(20 / span(xdom), 1, 1000)"
    }
  ],

  "data": [
    {
      "name": "points",
      "format": {
        "type": "csv"
      },
      "url": "https://gist.githubusercontent.com/neildeo05/1eaace0c48138020d1d88f53dcc239a3/raw/451ec8de369c14108d7902f1c0f89ea8082cd1dc/lotsofdata.csv",
      "transform": [
        { "type": "extent", "field": "Time", "signal": "xext" },
        { "type": "extent", "field": "Data", "signal": "yext" }
      ]
    }
  ],

  "scales": [
    {
      "name": "xscale", "zero": false,
      "domain": {"signal": "xdom"},
      "range": "width"
    },
    {
      "name": "yscale", "zero": false,
      "domain": {"signal": "ydom"},
      "range": "height"
    }
  ],

  "axes": [
    {
      "scale": "xscale",
      "orient": "bottom"
    },
    {
      "scale": "yscale",
      "orient": "left"
    }
  ],

  "marks": [
    {
      "type": "line",
      "from": {"data": "points"},
      "clip": true,
      "encode": {
        "enter": {
          "fillOpacity": {"value": 1.0},
          "fill": {"value": "steelblue"}
        },
        "update": {
          "x": {"scale": "xscale", "field": "Time"},
          "y": {"scale": "yscale", "field": "Data"},
          "size": {"signal": "size"}
        }
      }
    },
    {
      "type": "rect",
      "encode": {
        "enter": {
          "stroke": {"value": "#888"},
          "strokeDash": {"value": [3, 3]}
        },
        "update": {
          "strokeOpacity": {"signal": "box ? 0.3 : 0"},
          "x": {"signal": "(box) ? down[0]: 0"},
          "y": {"signal": "(box) ? down[1]: 0"},
          "x2": {"signal": "box ? box[0] : 0"},
          "y2": {"signal": "box ? box[1] : 0"}
        }
      }
    }
  ]
}


vegaEmbed('#vis', obj);




