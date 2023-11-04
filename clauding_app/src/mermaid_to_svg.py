import asyncio
from pyppeteer import launch

async def mermaid_to_svg(mermaid_code):
    browser = await launch()
    page = await browser.newPage()
    await page.setContent(f'<div class="mermaid">{mermaid_code}</div>')
    
    # Wait for a brief moment to ensure the diagram is fully rendered
    await asyncio.sleep(1)
    
    # Get the SVG content
    svg_content = await page.evaluate('document.querySelector("svg").outerHTML')
    
    await browser.close()
    return svg_content
