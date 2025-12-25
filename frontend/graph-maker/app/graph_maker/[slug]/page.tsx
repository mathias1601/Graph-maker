import FileReader from "@/components/FileReader";
import "../../../styles/mainPage.css"


export type Args = {
  params: Promise<{
    slug?: string
  }>
}

export default async function Page({ params: paramsPromise }: Args) {
  const { slug } = await paramsPromise;

  return (
    <div className="menu-div">
      <h1>{slug}</h1>
      <FileReader graphType={slug} />
    </div>
  );
}