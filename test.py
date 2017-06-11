import juliaset

renderer = juliaset.render.JuliaSetRenderer()
julia = juliaset.render.JuliaSet()
julia.center = juliaset.utility.Complex(0.43, -0.57)
julia.const = juliaset.utility.Complex(0.37, -0.084)
julia.window = 0.45
julia.color = juliaset.utility.JuliaSetColor(hue=0.04, brightness=0.0, saturation=1.0)
image = renderer.render(julia, (2560, 1600))
image.save('img.png')