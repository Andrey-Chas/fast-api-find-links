import re


def find_link_method_1(description):
    zoom_link_pattern = r'https:\/\/[\w-]*\.?zoom.us\/(j|my)\/[\d\w?=-]+'
    meets_link_pattern = r'https:\/\/meet\.google\.com\/[a-z]+-[a-z]+-[a-z]+'
    teams_link_pattern = r'https:\/\/teams\.microsoft\.com\/l\/meetup-join\/[a-zA-Z0-9\/%]+'

    zoom_match = re.search(zoom_link_pattern, description)
    if zoom_match:
        return zoom_match.group(0)

    teams_match = re.search(teams_link_pattern, description)
    if teams_match:
        return teams_match.group(0)

    meets_match = re.search(meets_link_pattern, description)
    if meets_match:
        return meets_match.group(0)

    return ""


def find_link_method_2(description):
    if description.startswith("https://zoom.us") or description.startswith("https://meet.google") or description\
            .startswith("https://teams.microsoft"):
        return description
    else:
        return ""
