import { graph } from '@/types/graphTypes'
import Link from 'next/link'

interface props {
    graph: graph
}

const Graphbutton = ( { graph }: props ) => {
  return (
    <div>
        <Link href={`/graph_maker/${graph.graphType}`}>
            <img src={graph.imgSrc} alt="" />
            <h2>{graph.name}</h2>
        </Link>
    </div>
  )
}

export default Graphbutton