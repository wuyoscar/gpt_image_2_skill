# Subject and Medium-Specific Analysis

Select the relevant sections according to the image’s actual type. Images with multiple subjects may combine multiple sections, but must not force in absent features.

## General Image

Cover the subject content, artistic or medium style, color scheme, lighting, composition logic, material qualities, camera language, spatial layers, mood, image-quality requirements, and detail treatment. The Chinese and English positive Prompts must have the same meaning; do not add new elements in the English version.

## People and Portrait Photography

Analyze clearly visible age cues and gender presentation, facial contour, features, hairstyle, makeup, expression, gaze, head angle, body orientation, posture, shoulder and neck position, hand and leg placement, body weight, the body part closest to the camera, perspective emphasis, clothing, accessories, skin texture, and the relationship between the person and the environment. When identity, age, or ethnicity cannot be judged reliably, describe only visible appearance and do not infer identity.

## Photography

Analyze natural, hard, soft, back, or studio light; depth of field and focus; wide-angle, natural-perspective, or telephoto-compression effects; cool/warm, vintage, commercial clarity, or film character; clarity, grain, noise, sharpness, and motion blur; and documentary, studio, casual snapshot, fashion portrait, or cinematic-still photography. Write specific camera parameters only with sufficient evidence; do not invent focal length, aperture, shutter speed, ISO, camera model, or photographer name.

## Product and Commercial Photography

Analyze product category, shape, color, orientation, share of frame, packaging structure, edges, buttons, ports, label position, surface material, specular highlights, roughness, transparency, shadow placement, props such as droplets/powder/liquid/steam/ice/petals, background arrangement, and which visible structures and materials communicate the product’s selling points. Do not generate clear brand logos, garbled packaging text, or nonexistent functional structures.

## Typography, Logos, and Text Design

Analyze modern, vintage, cyber, handwritten, minimal, or decorative style; letterform width, slant, roundness, geometry, and proportions; stroke weight, serif or sans-serif structure, bevels, cuts, connections, broken strokes, and negative space; letter spacing, line spacing, hierarchy, and layout logic; outlines, glow, gradients, embossing, shadows, and 3D effects; metal, matte, glass, plastic, neon, or paper materials; and the relationship among palette, composition, lighting, and background.

When a logo or text is a supporting element, translate it into an abstract symbol, simplified pattern, or blurred mark. Write specific text in the Prompt only when the user explicitly requests it and provides the content.

## Natural Landscapes and City Scenes

Analyze location and environment type, season, weather, dawn/day/dusk/blue hour/night, foreground/middle ground/background and horizon, sky/clouds/water/mist/atmospheric perspective, vegetation/mountains/buildings/streets/lights/reflections, street perspective lines and building geometry, light direction, warm/cool changes, depth of field, perspective, detail texture, and overall mood. Do not invent a specific location, city, or landmark from a vague visual effect.

## Architecture and Interior

Analyze space type and function, perspective direction, vanishing points, main lines, foreground/middle ground/background, architecture/furniture/wall/floor/decorative materials, natural/window/strip/ambient light sources, spatial scale, order and mood, whether the space should be tidy/empty/free of clutter, and the connection between interior and exterior or the view outside the windows.

## Illustration

When the image’s primary medium is hand-drawn, digital-painted, flat-shaded, painterly, watercolor, pencil, printmaking, vector, anime-style, children’s-book, or another illustration, continue reading and applying [illustration-style.md](illustration-style.md). This section separates subject content from style expression and prioritizes observable techniques such as line, shape, value, color, and texture. Do not use it to rewrite analysis rules for photography, 3D renders, product images, or other non-illustration types.

## 3D Rendering

Analyze realistic, semi-realistic, 3D cartoon, clay, toy, or minimalist style; modeling proportions, soft edges, and detail precision; matte, metal, glass, acrylic, resin, PVC, or ceramic materials; reflection, refraction, roughness, subsurface scattering, and PBR qualities; three-point, soft, rim, volumetric, or ambient light; shadow softness, contact shadows, antialiasing, and post-processing glow. Write C4D, Blender, Octane, or other software or renderer names only with sufficient evidence or when specified by the user; otherwise use general 3D-rendering language.

## IP Characters, Chibi, Collectible Toys, and Blind Boxes

Analyze chibi, collectible-toy, comforting, traditional-inspired, clay, or cartoon style; head-to-body ratio, body shape, silhouette, facial features, expression, hairstyle, demeanor, clothing, decorations, action, matte/resin/PVC/ceramic/clay qualities, soft light, solid-color background, display stand, product-like presentation, full-body design, and detail density. The final Prompt should describe the character’s visual features without depending on a specific IP or character name.

## Animals

Analyze animal type, body shape, fur/feather/scale color, posture, action, gaze, fur/feather/scale/skin/claw texture, relationship with the environment or other subjects, rim light, and overall mood. When the species cannot be identified reliably, describe visible posture and appearance without inventing a specific breed.

## Food

Analyze food type, main ingredients, shape, color, plating, share of frame, oily sheen, sauce, steam, crispness, moisture, cream, powder, frosting, stretch, drips, tableware, tabletop material, lighting, shadows, depth of field, shooting angle, and which colors, gloss, textures, and sense of temperature create appetite appeal.

## Vehicles

Analyze vehicle type, viewing angle, body or fuselage material, reflections, lights, highlight lines, stationary or moving state, road/sky/city/natural environment, and actually present effects such as speed lines, dust, splashes, or motion blur, as well as perspective and subject scale. By default exclude clear brand logos, license plates, numbers, and readable text.

## Plants and Flowers

Analyze plant type or visible form, color, quantity, growth state, petal/leaf/pollen/dew/texture, whether light passes through petals or leaves, foreground and background occlusion, blur, and the relationship with the background, as well as the concrete visual sources of softness, freshness, romance, or quietness.

## Graphic Posters and Visual Design

Analyze layout structure, main-visual position, color blocks, graphic elements, background relationships, negative space, grid, alignment, visual flow, foreground/background hierarchy, occlusion, proportions, text-area position and hierarchy, main/supporting/accent colors, grain, gradients, outlines, shadows, collage, or glitch effects. If the goal is to reproduce the layout rather than the text content, write “reserved text area”; if text is only a visual element, exclude clear readable text.

## Abstract Graphics and Mixed Subjects

Analyze basic geometry, curves, color blocks, textures, repetition, primary/secondary relationships, rhythm, balance, directionality, transparent overlays, glow, gradients, materials, and the distance, occlusion, proportions, and narrative relationships among multiple subjects. Combine only the specialized rules that are actually relevant; avoid writing every category’s features into the Prompt at once.
