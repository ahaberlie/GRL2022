import matplotlib.colors as colors
import json

def _parse_color_info(simulation, variable):

    with open("color_config.json", 'r') as f:
        colors = json.load(f)

    colors = colors[simulation][variable]

    d_colors = {list(i.keys())[0]: list(i.values())[0] for i in colors}

    return d_colors


def get_cmap(sim_name, var):

    color_info = _parse_color_info(sim_name, var)

    cmap_ = colors.ListedColormap(color_info['colors'])
    cmap_.set_under(color_info['under'])
    cmap_.set_over(color_info['over'])
    norm_ = colors.BoundaryNorm(color_info['values'], ncolors=cmap_.N)

    return norm_, cmap_
