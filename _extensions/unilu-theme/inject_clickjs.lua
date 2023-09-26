
local logo_url = nil

-- if the logo_url variable is not defined in header
-- set to point to quarto website
local function read_meta(meta)
  if meta["logo_url"] ~= nil then
    logo_url = meta["logo_url"]
  else
    logo_url = "https://quarto.org"
  end
end

local function process_body(doc)

  if quarto.doc.hasBootstrap() or quarto.doc.isFormat("revealjs") then
    local f = assert(io.open(quarto.utils.resolve_path("click-logo.html"), "r"))
    local click = f:read("*all")
    f:close()
    local outfile = os.tmpname()
    local o = assert(io.open(outfile, "w"))
    click = string.gsub(click, "XXX",  pandoc.utils.stringify(logo_url))
    o:write(click)
    -- could not make it to work with quarto.doc.include_text, so using a temp file
    quarto.doc.include_file("before-body", outfile)
    o:close()
  end
end

-- Run in two passes so we process metadata
-- and then process the doc
return {
  {Meta = read_meta},
  {Pandoc = process_body}
}