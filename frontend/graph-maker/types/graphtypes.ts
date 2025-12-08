export type graph = {
  graphType: string;
  name: string;
  imgSrc: string | undefined;
}

export const bargraph: graph = {
  graphType: "bar_graph",
  name: "BarGraph",
  imgSrc: undefined
}

export const boxplot: graph = {
  graphType: "box_plot",
  name: "BoxPlot",
  imgSrc: undefined
} 

export const violinplot: graph = {
  graphType: "violin_plot",
  name: "ViolinPlot",
  imgSrc: undefined
} 