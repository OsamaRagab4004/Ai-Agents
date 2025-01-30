from lxml import html
class HTMLcorrecter:
    def correct_html(self,html_code):
        # Parse the HTML
        parsed_html = html.fromstring(html_code)

        # Generate the corrected HTML
        corrected_html = html.tostring(parsed_html, pretty_print=True, method="html", encoding='unicode')

        return corrected_html

