

In an empty .leo file, setup the following outline node structure::

  + Startup
    + @settings
      + Menus
        + @menus
          + @menu File
            - @item new
            - @item open-outline 
            - @item file-open-by-name
            - @item save-file
            - @item save-file-to
            - @item close-window

For the body of the @item nodes, any text you enter will be used as the name of the menu item. Otherwise the name will be inferrred from the command itself.
