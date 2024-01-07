def generate_bar_chart(x:pd.Series,
                       y:pd.Series,
                       hue:pd.Series=None,
                       color_pallete:str='rocket_r',
                       size:tuple[int,int]=(12,8),
                       title:str=None,
                       save_img:bool=False):

    # set color pallete
    sns.set_palette(sns.color_palette(color_pallete))

    # set Chart size
    fig = plt.figure(figsize=size)

    # Barchart

    ax = sns.barplot(
            x=x,
            y=y,
            orient='v',
            saturation=1,
            width=0.75,
            hue=hue,
            errorbar=None
        )

    # Y-lables formatting
    ylabels = ['{:1.1f} $'.format(y) + 'K' for y in ax.get_yticks()/1000]
    ax.set_yticklabels(ylabels)

    # Adding Text Value labels on top of each bar
    show_values_on_bars(ax.axes)

    # If Hus Moving legend beyond the chart
    if hue is not None:
        sns.move_legend(
            ax, "upper left",
            bbox_to_anchor=(1.05, 1), borderaxespad=0)

    # Removing border around the chart
    plt.box(False)

    # Rotating X-lables
    ax.tick_params(axis='x', rotation=90)


    plt.title(title)
    plt.tight_layout()

    # Save to the current folder
    if save_img:
        img_name = f"{title}.jpg"
        plt.savefig(img_name, dpi='figure',bbox_inches='tight')

    plt.show()

    return ax
