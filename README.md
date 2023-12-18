# MUSA_5500_Final

**Using Yelp and Zillow Data to find Commercial Corridors in Philadelphia**

### Current Status

*   This repository currently has a `data` folder that houses webscraped data scraped from Zillow and will hopefully house the yelp and final cleaned datasets

### Rendering the website through Quarto

<!-- with docs/ removed from .gitignore, the normal flow works now -->
<!-->
*   Open the miniforge prompt and navigate just outside the MUSA_5500_Final repository folder 

*   Copy and paste the following code block to move problematic top-level files out and render in one go
    
    -   add any additional files to the list as needed via
    `move <filename here> files\ to\ move\ outside\ repo\ before-quarto_render_/ `


in Windows/Miniforge Prompt:
`move MUSA_5500_Final/README.md MUSA_5500_Final/files\ to\ move\ outside\ repo\ before-quarto_render_/ && move MUSA_5500_Final/files\ to\ move\ outside\ repo\ before-quarto_render_/  && cd MUSA_5500_Final && quarto render . && cd .. && move files\ to\ move\ outside\ repo\ before-quarto_render_/ MUSA_5500_Final `
    

or in Linux:
`move -t files\ to\ move\ outside\ repo\ before-quarto_render_/ README.md && mv files\ to\ move\ outside\ repo\ before-quarto_render_/ .. -r && quarto render . && mv ../files\ to\ move\ outside\ repo\ before-quarto_render_/ . -r && mv -t . files\ to\ move\ outside\ repo\ before-quarto_render_/*`

*   When we find out how to make quarto bypass executing certain markdowns and tell github how to specify landing page, `quarto render .` should suffice

    * there might be errors with the windows side
    -->
 
*   Open the miniforge prompt and navigate to the MUSA_5500_Final repository folder 

*   add appropriate ipynb files or folders with index.qmd to the repository
    -   then make appropriate section or contents references in top-level _quarto.yml
    -   *  run `quarto preview .` in the Miniforge Prompt to see you the changes look (you should be able to save files and changes will show up if already open)

*  run `quarto render .` in the Miniforge Prompt

*  add docs/ folder to github and push

**Your changes should now be viewable to all on the website give or take a few minutes!**


#### Problems

*   While I haven't tested all neighborhoods, some entries do not have any and my attempts to use OSM's Nominatim geocoding had problems for programmatic coordinate retrieval
    -   work in 'Webscraping Zillow Data.ipynb' currently
