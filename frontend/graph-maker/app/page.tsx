import FileReader from "@/components/FileReader";
import Graphbutton from "@/components/Graphbutton";
import { bargraph, boxplot, graph, violinplot } from "@/types/graphtypes";

export default function Home() {

  const graphTypes: graph[] = [
    bargraph,
    boxplot,
    violinplot
  ]

  const displayGraphButtons = graphTypes.map((graphType, index) => (
    <div key={index}>
      <Graphbutton graph={graphType}/>
    </div>
  ))

  return (
    <div>
      {displayGraphButtons}
    </div>
  );
}
